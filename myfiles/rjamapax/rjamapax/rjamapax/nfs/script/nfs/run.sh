#!/bin/bash
#it must be in an order: 1. Create SC, 2. Create PV, 3. Create PVC, 4. Create deployment, 5. Describe SC, 6. Describe PV, 7. Describe PVC, 8. Describe deployment, 9. Describe POD
export namespace=rjamapax
export nfsbase=/opt/vude/nfs 

function createSC () {
    echo " Creating SC for namespace $namespace"
    kubectl apply -f $nfsbase/storage -n $namespace
}

function createPV() {
    echo " Creating PV for namespace $namespace"
    kubectl apply -f $nfsbase/pv -n $namespace
}

function createPVC() {
    echo " Creating PVC for namespace $namespace"
    kubectl apply -f $nfsbase/pvc -n $namespace
}

function createdeployment() {
    echo " Creating deployment for namespace $namespace"
    kubectl apply -f $nfsbase/deployment -n $namespace
}

function createPOD() {
    echo " Creating POD for namespace $namespace"
    kubectl apply -f $nfsbase/pod -n $namespace
}

function describeSC() {
    echo " Describe SC for namespace $namespace"
    kubectl describe sc nfs-storage -n $namespace
}

function describePV() {
    echo " Describe PV for namespace $namespace"
    kubectl describe pv vude-pv -n $namespace
}

function describePVC() {
    echo " Describe PVC for namespace $namespace"
    kubectl describe pvc vude-pvc -n $namespace
}

function describedeployment() {
    echo " Describe deployment for namespace $namespace"
    kubectl describe deployment nginx-deployment -n $namespace

}

function describePOD() {
    echo " Describe POD for namespace $namespace"
    kubectl describe pod pod.yml -n $namespace
}

createSC
createPV
createPVC
createdeployment
createPOD
