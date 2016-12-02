# 对云API的简单封装

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
