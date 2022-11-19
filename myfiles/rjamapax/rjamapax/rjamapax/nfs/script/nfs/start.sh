# NOTES:

# create storageclass
kubectl apply -f storage.yml -n rjamapax
# get sc
kubectl get sc
# describe sc
kubectl describe sc

# create pv
kubectl apply -f pv.yml -n rjamapax
# get pv
kubectl get pv
# describe pv
kubectl describe pv vude-pv

# create pvc
kubectl apply -f pvc.yml -n rjamapax
# get pvc
kubectl get pvc -n rjamapax
# describe pvc
kubectl describe pvc vude-pvc -n rjamapax

# create deployment
kubectl apply -f dp.yml -n <<ns-name>>
# get deployment
kubectl get deployment <<deployment-name>> -n <<ns-name>>
# describe deployment
kubectl describe deployment <<deployment-name>> -n <<ns-name>>

# create pod
kubectl apply -f pod.yml -n rjamapax
# get pods
kubectl get pods vude-pod -n rjamapax
# describe pod
kubectl describe pod vude-pod -n rjamapax

# login to the pod
kubectl exec -it vude-pod -n rjamapax -- bash
ls /usr/share/nginx/html/
cat /usr/share/nginx/html/file111