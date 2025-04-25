.PHONY: kustomize-krakend-aws-dev
kustomize-krakend-aws-dev:
	kustomize build k8s/api-gateway/krakend/final/staging-aws > k8s/api-gateway/krakend/final/staging-aws/gitops/staging-jakarta.yaml

.PHONY: kustomize-krakend-aws-prod
kustomize-krakend-aws-prod:
	kustomize build k8s/api-gateway/krakend/final/production-aws > k8s/api-gateway/krakend/final/production-aws/gitops/production-jakarta.yaml

.PHONY: kustomize-krakend-docker-dev
kustomize-krakend-docker-dev:
	kustomize build k8s/api-gateway/krakend/final/staging-docker > k8s/api-gateway/krakend/final/staging-docker/gitops/staging-jakarta.yaml

.PHONY: kustomize-krakend-docker-prod
kustomize-krakend-docker-prod:
	kustomize build k8s/api-gateway/krakend/final/production-docker > k8s/api-gateway/krakend/final/production-docker/gitops/production-jakarta.yaml
