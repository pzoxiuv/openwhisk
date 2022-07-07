proxy:
	CGO_ENABLED=0 GOOS=linux GOARCH=amd64 GO111MODULE=auto go build -o proxy -a -ldflags "-extldflags=-static" proxy.go 