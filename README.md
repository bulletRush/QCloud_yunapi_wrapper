# 对云API的简单封装

## **NOTICE**

* **本项目代码未实际用于生产环境，仅供参考**
* **example下的代码仅供参考，如需使用，请自行修改**

## 使用步骤

### 设置`PYTHONPATH`

```shell
YUN_API_WRAPPER_PATH=<your path here>
export PYTHONPATH='${YUN_API_WRAPPER_PATH}：${YUN_API_WRAPPER_PATH}/thirdparty:${PYTHONPATH}'
```

或者直接运行`init.sh`

### 修改示例程序

```shell
mv example/config.py.example example/config.py
```

修改`example/config.py`中的`secretId`和`secretKey`为自己的配置。然后运行`python example/cbs_example.py`查看效果。


## Q&A

### 查询磁盘使用率和iostat数据时，disk和diskname参数的区别？

* disk指的是你的磁盘，目前对于系统盘传入root，随子机购买的数据盘传入data；独立云盘传入云盘实例ID（即disk-xxxx）
* diskname指的是你的磁盘的分区，可以通过`cvm.describe_instance_disk_names`查询diskname，示例见`example/cvm_example.py`


