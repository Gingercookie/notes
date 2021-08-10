# Practice Test 1

### Commands
- `kubectl run nginx-pod --image=nginx:alpine`
- `kubectl run messaging --image=redis:alpine --labels="tier=msg"`
- `kubectl create namespace apx-x9984574`
- `kubectl get nodes -o json > /opt/outputs/nodes-z3444kd9.json`
- `kubectl expose pod messaging --type=ClusterIP --name=messaging-service --port=6379`
- `kubectl create deployment hr-web-app --image=kodekloud/webapp-color --replicas=2`
- `kubectl run temp-bus --image=redis:alpine -n finance`
- `kubectl expose deployment hr-web-app --type=NodePort --port=8080 --target-port=30082 --name=hr-web-app-service`
- `kubectl get pod orange -o yaml > orange.yaml`
- `vim orange.yaml && kubectl apply -f orange.yaml`

### Static Pods
Static pods run in a directory - defined as `staticPodPath`, defined in the `/var/lib/kubelet/config.yaml` on each node. (Each node runs a kubelet, and should have this defined)

### JSON PATH
Learn JSON PATH

# Practice Test 2
1. Backup an ETCD cluster (API v2 and v3 have different commands)
  - v2 : `etcdctl backup ...`
  - v3 : `etcdctl snapshot save <dir>`
2. Create a pod with emptyDir volume
  - Search k8s docs for `emptyDir`, there is an example
  - [link](https://kubernetes.io/docs/concepts/storage/volumes/)
3. Set security capabilities for a container  
  - [link](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)
4. Revisit the part on persistent volumes and persistent volume claims
  - [link](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)
5. Create a deployment and perform a rolling update on it.
6. Create user X with access to Y methods within Z namespace.
7. DNS resolution for an internally exposed (ClusterIP?) service.
8. Static pod created 
