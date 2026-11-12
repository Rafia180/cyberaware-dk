"""
main.py - the heart of the website.

FastAPI is the library that turns Python functions into web pages.
Each function below that has @app.get("...") above it is ONE page:
when someone visits that address, FastAPI runs the function, and the
function sends back a finished HTML page.

How to read a route:
    @app.get("/about")          <- the web address, e.g. 127.0.0.1:8000/about
    def about(request):         <- the Python function that builds the page
        return templates...     <- fill in an HTML template and send it back

There is no database. Every page gets its words straight from
content.py, which Python loads into memory once, when the server starts.
"""

# ---------------------------------------------------------------------
# Imports: bring in the tools we need from other files and libraries.
# ---------------------------------------------------------------------

# FastAPI is the web framework. HTTPException lets us send a
# "404 page not found" error. Request holds details of the visit,
# such as which address was asked for.
from fastapi import FastAPI, HTTPException, Request

# StaticFiles serves files that never change, like our CSS and JS.
from fastapi.staticfiles import StaticFiles

# Jinja2Templates fills in our HTML templates with real data.
from fastapi.templating import Jinja2Templates

# Our own file in this folder: all the words on the site.
from app.content import (
    CORE_RULES,
    EMERGENCY_STEPS,
    HELP_CHANNELS,
    TOPICS,
    get_topic,
)


# Create the web application itself.
app = FastAPI(title="CyberAware DK")

# Anything in the "static" folder is served at /static/...
# For example static/css/style.css is reachable at /static/css/style.css
app.mount("/static", StaticFiles(directory="static"), name="static")

# Tell Jinja2 where our HTML templates live.
templates = Jinja2Templates(directory="templates")


# ---------------------------------------------------------------------
# The pages (routes).
#
# Version note: current FastAPI expects "request" as the FIRST thing
# given to TemplateResponse, like this:
#     templates.TemplateResponse(request, "page.html", {...})
# Old tutorials write TemplateResponse("page.html", {"request": request}).
# That old style now fails with: TypeError: unhashable type: 'dict'
#
# IMPORTANT: a template can only show what its route passes to it.
# If a route forgets to pass something, Jinja2 does NOT crash: it just
# shows nothing in that spot. So a heading can appear with an empty
# list under it. Check every page after changing a route.
# ---------------------------------------------------------------------

@app.get("/")
def home(request: Request):
    """The Home page. Fixed text only, so no data is passed."""
    return templates.TemplateResponse(request, "index.html")


@app.get("/learn")
def learn(request: Request):
    """The Learn page: the eight rules, then a card for each topic."""
    return templates.TemplateResponse(
        request, "learn.html",
        {"topics": TOPICS, "rules": CORE_RULES},
    )


@app.get("/learn/{slug}")
def topic_detail(request: Request, slug: str):
    """
    One topic page, e.g. /learn/housing-scams

    {slug} in the address is a placeholder. Whatever the visitor typed
    in that position arrives in the "slug" variable.
    """
    topic = get_topic(slug)

    # No topic with that name: show a "404 not found" error.
    if topic is None:
        raise HTTPException(status_code=404, detail="Topic not found")

    return templates.TemplateResponse(
        request, "topic_detail.html", {"topic": topic}
    )


@app.get("/get-help")
def get_help(request: Request):
    """The Get Help page: the emergency steps and the official contacts."""
    return templates.TemplateResponse(
        request, "get_help.html",
        {"steps": EMERGENCY_STEPS, "channels": HELP_CHANNELS},
    )


@app.get("/about")
def about(request: Request):
    """The About page. Fixed text only, so no data is passed."""
    return templates.TemplateResponse(request, "about.html")