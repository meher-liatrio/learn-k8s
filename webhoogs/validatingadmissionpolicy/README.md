
Before you begin

- Ensure the ValidatingAdmissionPolicy feature gate is enabled.
- Ensure that the admissionregistration.k8s.io/v1beta1 API is enabled.

`kind create cluster --name vap --image=kindest/node:v1.30.0`


when uncertain:

`k8s explain kindName`
`k8s explain ValidatingAdmissionPolicyBinding.spec.matchResources`