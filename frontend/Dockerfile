# Use a lightweight web server for static files
FROM nginx:alpine

# Copy the HTML and JavaScript files to the Nginx server
COPY index.html /usr/share/nginx/html/
COPY script.js /usr/share/nginx/html/

# Expose port 80 for the web server
EXPOSE 80

# Nginx will start automatically
