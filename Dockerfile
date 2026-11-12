# =====================================================================
# Dockerfile - the recipe Docker follows to build a "container image":
# a small, self-contained Linux computer with Python and this website
# inside it. Anyone with Docker can then run the site with one command,
# without installing Python or any packages themselves.
#
# Docker reads this file from top to bottom, one instruction at a time.
# =====================================================================

# Start from an official image that already has Python 3.12 installed.
# "slim" is a smaller version with only what Python needs.
FROM python:3.12-slim

# Work inside a folder called /app in the container.
# (It is created automatically. Every command below runs from here.)
WORKDIR /app

# Copy ONLY the list of packages first, then install them.
# Docker remembers ("caches") each step. Because requirements.txt rarely
# changes, the slow install step is reused on later builds, even when
# you change the website's code.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Now copy the website itself into the container.
COPY app ./app
COPY templates ./templates
COPY static ./static

# Security: do not run the website as "root" (the all-powerful admin
# user). Create an ordinary user with no special rights and switch to it.
RUN useradd --create-home appuser
USER appuser

# Document that the website listens on port 8000 inside the container.
EXPOSE 8000

# The command that starts the website when the container starts.
# --host 0.0.0.0 means "accept visits from outside the container",
# which is needed so your browser can reach it.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]