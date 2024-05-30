# Webhooks in kubernetes

# validating webhook:

- Why would pods 2, 4 and 5 pass as opposed to the rest of them? (Deliverable)
    the test 2 pod is in the `myapp` namespace,
    test 4,5 are in the default namespace, and so are not checked
    test 1 container is `myapp:1.24.0` instead of `myapp:latest`
    test 3 and all the rest also have containers that aren't `myapp:latest`