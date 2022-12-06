Example:
```
from hadoop_util import hadoop_wrapper 

hdfs_helper = hadoop_wrapper.HdfsHelper(hadoop_home='xxx/bin/hadoop')
hdfs_helper.ls()
hdfs_helper.get(afs_path, local_path)
...
```