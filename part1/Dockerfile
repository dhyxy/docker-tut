FROM nginx:alpine
# nginx servers files at /usr/share/nginx/html on port 80
# which is why we do `-p 80:80`

COPY index.html /usr/share/nginx/html

# the `sed` command below replaces text in the specified file, uncomment and see
# that the command is isolated to the docker image
RUN sed -i 's/diddy/lebron/' /usr/share/nginx/html/index.html


# docker build . -t part1
# docker run -p 80:80 part1