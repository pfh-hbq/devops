## CI 💯 practices
* Split work between phases

* Use job filters on branch names and tags
* Declare environment variables close to their usage
* Cache installed tools and dependencies
* Use a custom base image with all necessary tools installed
* When using third-party operations, bind them to the commit SHA so that they will not be maliciously changed
* Minimize operations: smaller size and avoid wasting time on unnecessary things
* Don't store passwords in the code
* Use job dependency
* Try to avoid script injection attacks
* Consider not to use self-hosted runners in public repositories

## Jenkins 💯 practices
* Correctly set the credentials of external services such as GitHub to achieve efficient access
* Use the docker agent to run jobs in it