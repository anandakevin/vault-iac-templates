.PHONY: kustomize-krakend-dev
kustomize-krakend-dev:
	kustomize build k8s/api-gateway/krakend/final/staging > k8s/api-gateway/krakend/final/staging/gitops/staging-jakarta.yaml

.PHONY: kustomize-krakend-prod
kustomize-krakend-prod:
	kustomize build k8s/api-gateway/krakend/final/production > k8s/api-gateway/krakend/final/production/gitops/production-jakarta.yaml
