# Use the official lightweight Python image.
FROM python:3.11

# Copy local code to the container image.

ENV APP_HOME /app
WORKDIR $APP_HOME

# Copy local code to the container image.
COPY . ./
pyvenv.cfg

# Install production dependencies.
RUN pip install -r requirements.txt

# Expose the port that the application will run on.
EXPOSE 8080

# Run the command to start the application.
CMD python app.py