#!/bin/bash
curl -X POST http://localhost:8080/invocations \
    -H "Content-Type: application/json" \
    -d '{"prompt": "who invented the lightbulb?"}'