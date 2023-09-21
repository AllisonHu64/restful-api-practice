#!/bin/bash
set -x

# System control will return either "active" or "inactive".
tomcat_running=$(systemctl is-active flask)
if [ "$tomcat_running" == "active" ]; then
    service flask stop
fi