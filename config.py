import os

# 静态文件路径
staticPath = os.path.join(os.path.dirname(__file__), 'static')

# 场景状态
screenList = {
    '新版大厅': None,
    '服务器列表': None,
    '频道列表': None,
    '房间列表': None,
    '房间': None,
    '加载中': None,
    '游戏中': None,
    '结算中': None,
}

