# coding:utf-8

SEX_CHOICES = {
    '0': '女',
    '1': '男',
    '2': '其他',
}

rsp_data = {
    'SUCESS'
}

ERROR = {
    'SUCC': {'code': '10000', 'msg': u'成功'},
    'ERROR': {'code': '10001', 'msg': u'未知错误'},
    'PARA_ERR': {'code': '10002', 'msg': u'表单参数错误'},
    'NOT_EXIST_ERR': {'code': '10003', 'msg': u'记录不存在'},
    'PERM_ERR': {'code': '10004', 'msg': u'没有权限进行该操作'},
    'SYS_ERR': {'code': '10005', 'msg': u'系统繁忙'},
    'EXIST_ERR': {'code': '10006', 'msg': u'记录已存在'},
    'FORBIDDEN': {'code': '10007', 'msg': u'被禁止'},
    'MAINTAINANCE': {'code': '10008', 'msg': u'功能维护'},
    'IFUWO_RENDER_ERR': {'code': '10009', 'msg': u'渲染任务过多'},
    'FORBIDDEN_WORD_ERR': {'code': '10010', 'msg': u'内容中包含敏感词'},
    'STATE_ERR': {'code': '10011', 'msg': u'状态错误'},
    'VERIFYCODE_ERR':{'code': '10012', 'msg': u'验证码错误'},
    'NUM_LIMIT_ERR': {'code': '10013', 'msg': u'超出数量限制'},
    'OVERFLOW_MAX_LENGTH_ERR': {'code': '10014', 'msg': u'超出内容长度限制'},
    'SPHINX_STATUS_ERR': {'code': '10015', 'msg': u'sphinx状态错误'},
    'UNSUPPORT_ERR': {'code': '10016', 'msg': u'不支持该功能'},
}