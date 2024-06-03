
# Create cluster

`kind create cluster -n kyverno`

# Kaverno

- install kaverno in the cluster

`kubectl create -f https://github.com/kyverno/kyverno/releases/download/v1.12.0/install.yaml`

# Write and apply policy

`kubectl apply -f validate.yaml`
`kubectl apply -f mutate.yaml`

# Policy reports

`kubectl get policyreport -A`