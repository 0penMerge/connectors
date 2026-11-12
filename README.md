# OpenMerge connectors

This repository holds connector source managed through OpenMerge.
Changes are made on review branches and merged through pull requests.

## Layout

```
connectors/<name>/plugin.py        # connector implementation
connectors/<name>/connector.yaml   # connector manifest
connectors/<name>/schema.yaml      # data schema
catalog/default/<category>/*.json  # catalog entries
```

Create a connector bundle with the OpenMerge CLI, commit it on a branch,
and open a pull request. Then pull the branch in OpenMerge to edit it.
