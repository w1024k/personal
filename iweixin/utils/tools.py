# coding:utf-8
import uuid


def create_uuid():
    return str(uuid.uuid1()).replace('-', '')
