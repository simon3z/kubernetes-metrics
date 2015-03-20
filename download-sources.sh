#!/bin/sh

for pkg in heapster grafana; do
  pushd ./packages/$pkg
    wget $(rpmspec -P ${pkg}.spec | awk '/^Source0/{print $2}')
    md5sum -c sources
  popd
done
