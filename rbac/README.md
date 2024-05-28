helm repo add jenkins https://charts.jenkins.io
helm repo update
helm install jenkins jenkins/jenkins -n jenkins --version 5.1.24
kubectl get secret jenkins -n jenkins -o jsonpath="{.data.jenkins-admin-password}" | base64 --decode
kubectl get secret jenkins -n jenkins -o jsonpath="{.data.jenkins-admin-user}" | base64 --decode

kubectl port-forward svc/jenkins 8080:8080 -n jenkins



# Create a namespace named "test-rbac"
kubectl create namespace test-rbac

# Create a service account named "fluentd" in the "test-rbac" namespace
kubectl create serviceaccount fluentd -n test-rbac

# Create a cluster role "fluentd" with the ability to get, list, and watch pods and namespaces
kubectl create clusterrole fluentd --verb=get,list,watch --resource=pods,namespaces

# Create a cluster role binding "fluentd" configured to use the service account and role you just created
kubectl create clusterrolebinding fluentd --clusterrole=fluentd --serviceaccount=test-rbac:fluentd


# Check access.

kubectl auth can-i list namespaces --as system:serviceaccount:test-rbac:fluentd
kubectl auth can-i watch pods --as system:serviceaccount:test-rbac:fluentd
kubectl auth can-i delete secrets --as system:serviceaccount:test-rbac:fluentd
kubectl auth can-i --list --as system:serviceaccount:test-rbac:fluentd

# deliverables:
- Determine whether it's possible to add deny rules to roles.

    >In Kubernetes, roles and cluster roles are used to grant permissions, not to deny them. The Role-Based Access Control (RBAC) system in Kubernetes does not support deny rules. When a request is made, the system checks all the roles that apply to the user making the request, and if any of those roles grant the necessary permission, the request is allowed. If no roles grant the necessary permission, the request is denied. There is no way to create a role that explicitly denies a permission.
    
- What service account is a pod assigned if one is not specified? Why must a pod always have a service account configured?

    >If a service account is not explicitly assigned to a pod, the pod is assigned the default service account in the same namespace.
    
    >A pod must always have a service account configured because service accounts provide an identity for processes that run in a Pod. This allows the Kubernetes API to provide access control for those processes and enables processes to communicate with the Kubernetes API.