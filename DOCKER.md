### **Dockerfile 💯 practices**


- Don’t install unnecessary packages, use light base image
- Use .dockerignore to exclude unnecessary files
- Leverage build cache (Use --no-cache-dir)
- Minimize the number of layers, since Docker runs with the layers, the layers that are rarely changed are moved to the top to improve the cache of the build.
- Use linter to apply best practice to Docker images
- Prevent confidential data leaks (Do not put any credentials, use COPY over ADD)
- Use the health check of the application to view the current status
