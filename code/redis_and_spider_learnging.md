# redis

## 介绍

### 特点与有点

* 开源的，使用c编写，基于内存且支持持久化
* 高性能的key-value的NoSQL数据库
* 支持数据类型丰富，字符串strings，散列hashes，列表lists，集合sets，有序集合sorted sets等等
* 支持多种编程语言

### 其他数据库对比

* MySQL：关系型数据库，表格，基于磁盘，慢
* MongoDB：键值对文档型数据库，值为JSON文档，基于磁盘，慢，存储数据类型单一

注：redis的诞生接捐了磁盘IO带来的性能瓶颈

### 应用场景

* 使用redis来缓存一些经常被使用到，或者需要耗费大量资源的内容，通过这些内容放到redis里面，程序可以快速读取这些内容
* 一个网站，如果某个页面经常会被访问到，或者创建页面时消耗的资源比较多，比如需要多次访问数据库，生成时间比较长等，我们可以使用redis将这个页面缓存起来，减轻网站负担，降低网站的延迟，比如网站首页等

注：redis诞生是为了解决负载问题

### 附加功能

* 持久化：将内存中数据保存到磁盘中，保证数据安全，方便进行数据备份与恢复
* 过期键功能：为键设置一个过期时间，让它再指定时间内自动删除，以节省内存空间
* 事务功能：原子的执行多个操作
* 主从复制
* Sentinal哨兵

## 安装

* Ubuntu中
    ```shell
    # 安装
    sudo apt-get install redis-server
    # 服务端启动
    sudo /etc/init.d/redis-server status/start/stop/restart
    # 客户端连接
    redis-cil -h IP地址 -p 端口 -a 密码
    ```

* Windows中
    ```txt
    1. 下载安装包地址
    https://github.com/ServiceStack/redis-windows/blob/master/downloads
    2. 解压
    3. 启动服务端：双击解压后的redis-server.exe
    4. 客户端连接：双击解压后的redis-cil.exe
    5. 安装到本地服务
        1. 重命名 redis.window.conf 为 redis.conf，作为redis服务的配置文件
        2. cmd命令行进入到redis-server.exe所在目录
        3. 执行：./redis-server --service-install redis.conf --loglevel verbose
        4. 计算机-管理-服务-Redis-启动
    6. 客户端添加环境变量
    7. 卸载：到redis-sever.exe所在目录执行
        1. redis-server --service-uninstall
        2. sc delete Redis
    ```

## 日志

地址为```/var/log/redis/redis-server.log```

## 配置文件

### 所在路径

* Ubuntu：/etc/redis/redis.conf
* Windows：下载解压后的redis文件夹中，文件名为redis.windows.conf / redis.conf

### 设置连接密码

1. 找到requirepass，并在之后空格隔开后写上密码
2. 重启服务
3. 客户端连接

### 允许远程连接

1. 找到bind 127.0.0.1 ::1，注释掉本地IP地址绑定
2. 找到protected-mode，将后面的yes改为no，关闭保护模式
3. 重启服务

### 设置日志文件

日志文件配置：```logfile /var/log/redis/redis-server.log```

## 命令与数据类型

### 通用命令

```redis
# 切换库（number在0-15之间，db0~db15）
select number
# 查看键
keys 正则表达式/*
# 查看数据类型
TYPE key
# 键是否存在
exists key
# 删除键
del key
# 键重命名
rename key newkey
# 设置已有key的过期时间，单位s
expire key number
# 设置已有key的过期时间，单位ms
pexpire key number
# 查看key的存活时间
ttl key
# 删除过期时间
persist key
# 清除当前库中所有数据（慎用）
flushdb
# 清除所有库中所有数据（慎用）
flushall
```

### 字符串类型

#### 特点

* 字符串，数字，都会转化为字符串来存储
* 以二进制的方式存储在内存中

#### 命令

```redis
# 设置一个key-value
set key value [nx] [ex number] [px number] # 当有nx时表示，键不存在才会创建，存在则不做任何事；ex处可写过期时间，单位为s；px处可写过期时间，单位为ms
# 获取一个key的value
get key
# 设置若干个key-value
mset key1 value1 key2 value2
# 获取若干个key的value
mget key1 key2 key3
# 获取一个key的长度
strlen key
# 返回旧值并设置新值（如果键不存在就创建并赋值）
getset key value
# 存储的数字增加步长的值
incryby key 步长
# 存储的数字增加1
incy key
# 存储的数字减少步长的值
decryby key 步长
# 存储的数字减少1
decry key
# 增加或减少存储的数字浮点数的步长（为正增加，为负减少）
incrybyfloat key number 
```

#### 注意事项

* key值不易过长或过短，过长占用内存大，过小可读性差
* 一个字符串类型的值最多能存储512Mb的内容

### 列表类型

#### 特点

* 元素是字符串类型
* 列表头尾增删快，中间增删慢，增删元素是常态
* 元素可重复
* 最多可包含2^32 - 1个元素
* 索引同python列表

#### 命令

```redis
# 从头部压入元素
LPUSH key value1 value2
# 从列表尾部压入元素
RPUSH key value1 value2
# 在列表1尾部弹出一个元素，压入到列表2的头部
RPOPLPUSH key1 key2
# 在列表指定元素前/后插入元素
LINSERT key after|before value newvalue
# 查看列表中元素
LRANGE key start stop
# 获取列表长度
LLEN key
# 从列表头部弹出一个元素
LPOP key
# 从列表尾部弹出一个元素
RPOP key
# 列表头部阻塞弹出一个元素，列表为空时阻塞（timeout为0时会在列表为空时一直阻塞）
BLPOP key timeout
# 列表尾部阻塞弹出一个元素，列表为空时阻塞（timeout为0时会在列表为空时一直阻塞）
BRPOP key timeout
# 删除指定元素
LREM key count value # count>0时表示从头到尾；count<0表示从尾向头，移除与value值相等的元素，数量为count。count=0表示移除表中所有与value值相同的元素
# 保留指定范围内的元素
LTRIM key start stop
# 改列表中指定元素
LSET key index newvalue
```

### 哈希类型

#### 定义

* 有field和关联的value组成的键值对
* field和value时字符串列星
* 一个hash中最多包含2^32 - 1个键值对

#### 优点

节约内存空间并加快操作速度减少cpu计算压力，原因如下
  * 每创建一个键，它都会为这个键存储一些附加的管理信息（比如这个键的类型，这个键最后一次被访问的时间等）
  * 键越多，redis数据库在储存附件管理信息方面耗费内存越多，花在管理数据库键上的cpu资源也会越多

#### 缺点

* 位图操作不能使用散列类型数据
* 无法对散列中的字段单独设置过期时间，只能对整个散列对象设置过期时间

#### 命令

```redis
# 设置单个字段
HSET key field value
# 在字段不存在时，设置单个字段，否则什么都不做
HSETNX key field value
# 返回字段个数
HLEN key
# 判断字段是否存在（返回值为0或1）
HEXISTS key field
# 返回单个字段的值
HGET key field
# 返回多个字段的值
HMGET key field1 field2 ...
# 返回所有键值对
HGETALL key
# 返回所有字段名
HKEYS key
# 返回所有值
HVALS key
# 删除指定字段
HDEL key field
# 在字段对应值上进行整数增量运算，值为负时为减少
HINCRBY key field increment
# 在字段对应值上进行浮点数增量运算，值为负时为减少
HINCRBYFLOAT key field increment
```

### 集合类型（set）

#### 特点

* 去重无序
* 元素是字符串类型
* 最多包含2^32 - 1个元素

#### 命令

```redis
# 增加一个或多个元素，自动去重
SADD key member1 member2 ...
# 查看集合中所有元素
SMEMBERS key
# 删除一个或者多个元素，元素不存在自动忽略
SREM key member1 member2 ...
# 元素是否存在
SISMEMBER key member
# 随机返回集合中指定个数的元素，默认为1个
SRANDMEMBER key [count]
# 弹出成员
SPOP key [count]
# 返回集合中元素的个数
SCARD key
# 把元素从集合1移动到集合2
SMOVE key1 key2 member
# 差集
SDIFF key1 key2
# 差集并保存到新集合中
SDIFFSTORE key key1 key2
# 交集
SINTER key1 key2
# 交集并保存到新集合中
SINTERSTORE key key1 key2
# 并集
SUNION key1 key2
# 并集并保存到新集合中
SUNIONSTORE key key1 key2
```

### 有序集合（sortedset）

#### 特点

* 有序去重
* 元素是字符串类型
* 每个元素关联一个浮点数分值（score），并按照分值从小到大的顺序排列集合中的元素（分值可以相同）
* 最多包含2^32 - 1个元素

#### 命令

```redis
# 在有序集合中添加一个成员
zadd key score member
# 查看指定区间元素（升序）
zrange key start stop [withscores] # 有withscores会有分数，反之只显示成员
# 查看指定区间元素（降序）
ZREVRANGE key start stop [withscores] # start stop为索引区间
# 查看指定元素的分值
ZSCORE key member
# 返回指定区间元素
zrangebyscore key min max [withscores] [limit offset count] # min max为分值区间，数字左侧加圆括号表示取不到；有limit关键词时，offset是跳过多少元素，count意为返回几个
# 删除成员
zrem key member
# 增加或者减少分值
zincrby key increment member
# 返回元素排名
zrank key member
# 返回元素逆序排名
zrevrank key member
# 删除指定区间内的元素
zremrangebyscore key min max
# 返回集合中元素个数
zcard key
# 返回指定范围中的元素个数
zcount key min max
# 并集
zunionstore key numkeys key1 key2 ... [weights 权重值] [AGGREGATE SUM（默认）|MIN|MAX] # numkeys是要取并集的集合个数；权重值表示每一个集合中的分数会先乘以权重再处理；AGGREGATE表示处理的方式，SUM求和MIN取最小MAX取最大
# 交集
ZINTERSTORE key numkeys key1 key2 ... [WEITHTS weight] [AGGREGATE SUM（默认）|MIN|MAX]
```

### 位图操作

#### 定义

* 位图不是真正的数据类型，它是定义在字符串类型中的
* 位图上限为2^32

#### 优点

在统计用户活跃度上（主要应用），其节省空间并且统计速度快

#### 命令

```redis
# 设置某一位上的值
setbit key offset value # offset为偏移量，从0开始；值为0或1；如果设置时key的长度小于设置的偏移量，那么默认以0填充
# 获取某一位上的值
GETBIT key offset
# 统计键所对应的值有多少个1
BITCOUNT key
```

## 数据持久化

### 定义

将数据从掉电易失的内存放到永久存储的设备上

### 数据持久化模式

#### RDB模式（默认开启）

##### 特点

* 保存真实的数据
* 将服务器包含的所有数据库数据以二进制文件的形式保存到硬盘里面
* 默认文件名 /var/lib/redis/dump.rdb

##### 创建rdb文件的两种方式

* 服务器执行客户端发送的SAVE或者BGSAVE命令
    * 特点：SAVE会阻塞redis服务，BGSAVE不会阻塞redis服务
    * 如果rdb文件已存在，那么服务器将自动使用新的rdb文件代替旧的rdb文件
    * 配置文件操作：
      * dir /var/lib/redis # 为rdb文件存放地址
      * dbfilename dump.rdb # 文件名
* 设置配置文件条件满足时自动保存，可以修改、添加、减少
  ```txt
  # 下方若干的条件中只要满足其中一个就会执行自动保存
  save 900 1 # 第一个数字表示至少过去多少时间，第二个数字表示至少执行的操作次数，只有当两个条件同时满足时才会出发自动保存
  save 300 10
  save 60 10000

  # 注：以上若干条件当有一个满足后，计时器与计次器都会清零
  ``` 

#### AOF模式

##### 特点

* 存储的是命令，而不是真实数据
* 默认不开启

##### 开启方式（配置文件中设置）

1. 找到appendonly，把后面的no改为yes
2. 找到appendfilename，可以在后面修改保存的文件名
3. 重启服务

##### RDB缺点

创建rdb文件需要将服务器所有的数据库的数据都保存起来，极其耗费资源和时间，所以服务器需要隔一段时间才能够创建一个新的rdb文件，也就是说rdb文件不能执行的过于频繁，否则会严重影响服务器的性能，故可能会丢失数据

##### AOF的原理以及优点

* 原理：每当有修改数据库的命令被执行时，服务器就会将执行的命令写入到AOF文件的末尾
* 优点：用户可以根据自己的需要对AOF持久化进行调整，让redis在遭遇意外停机时不会丢失任何数据或者之丢失极其短时间的数据

##### AOF的相关策略（配置文件）

* 策略产生的目的：由于操作系统中并不会及时将要写入硬盘的数据写入，而是放在缓存区，所以为了保证数据的安全性，AOF提供了一些策略来解决该问题
* 找到配置文件中的appendfsync，有三个选项分别是always，everysec和no，其中everysec是默认开启的

注：一般always使用比较多

##### AOF文件中冗余命令的处理方式

* 特点：
  * 在执行重写时不会阻塞
  * 重写后的AOF文件的大小一般会变小，同时复原后的数据与重写前文件复原的数据一致
* 重写方法触发
  * 客户端向服务器发送BGREWRITEAOF命令
  * 修改配置文件使得能够自动执行
    * auto-aof-rewrite-percentage 100
    * auto-aof-rewrite-min-size 64mb
    * 解释：只有当AOF文件的增量达到百分百才会进行重写，第一触发为64mb，第二次触发为128mb，第三次触发为256mb，以此类推

#### 数据恢复（自动）

如果同时有adb文件与aof文件，会优先使用aof文件

## 主从复制

### 定义

* 一个redis服务可以有多个该服务的复制品，这个redis服务会成为master，其他复制品成为slaves
* master会一直将自己的数据更新同步给slaves，保持主从同步
* 只有master可以执行写命令，slave只能执行读命令

### 作用

从服务器执行客户端发送的读命令，客户端可以连接slaves执行读请求，分担了master读的高并发压力

### 实现方式

#### 命令行实现

```shell
redis-server --slaveof <master-ip><master-port>
```

#### redis命令行实现

```redis
slaveof IP PORT # 设置为某个主的从
slaveof no one # 解除设置为从
```

#### 修改配置文件实现

* 在配置文件的最后写上```slaveof IP PORT```
* 重启redis服务

### master挂了的处理方式

#### 手动处理

1. 一个slave执行slaveof no one命令
2. 其他slave执行slaveof NEWIP NEWPORT

#### 哨兵（sentinel）

##### 原理

* sentinel会不断检查master和slaves是否正常
* 每一个sentinel可以监控任意多个master和该master下的slaves

##### 安装

```shell
sudo apt install redis-sentinel
```

##### 配置文件

```txt
port xxxx
Sentinel monitor name IP PORT number # name任写即可；number表示当有若干哨兵同时监控时，只有当大于等于number数量的哨兵认为主挂掉时才会更改主从关系
```

##### 启动

```shell
redis-sentinel sentinel.conf
redis-server sentinel.conf --sentinel
```

注：当哨兵更换主从关系时，原本的主也会变为从，而且哨兵将服务器设置为从的关系时，是直接在配置文件中修改

## 分布式锁

### 出现原因

若干进程操作数据库时，可能导致数据库的存储出现异常

### 原理

* 客户端只有在redis数据库中获得锁时，才能操作数据库
* 其他客户端必须等待拿到锁的客户端释放锁后，才能再次抢夺

## python中的库（redis库）

### 安装

```shell
pip3 install redis 
```

### 使用

```python
import redis

# 数据库连接对象
r = redis.Redis(host="127.0.0.1", port=6379, db=0, password="123456")
# 查看所有key
r.keys("*") # 返回值结构为[b'xxx', b'xxx', ...]
# 查看key的数据类型
r.type("key") # 返回值为一个b串
# 查看key是否存在
r.exists("key") # 返回值为0或者1
# 设置key的过期时间
r.expire("key", timeout)
# 删除key
r.delete("key1", "key2", ...)
# 列表左侧压入一个元素
r.lpush("key", "value1", "value2", ...)
# 列表右侧压入一个元素
r.rpush("key", "value1", "value2", ...)
# 列表中的某个元素前后插入一个元素
r.linsert("key", "before"|"after", "oldvalue", "newvalue")
# 查看列表长度
r.llen("key")
# 查看列表指定范围元素
r.lrange("key", start, stop)
# 列表右侧弹出一个元素
r.rpop("key")
# 列表右侧阻塞弹出一个元素
r.brpop("key", timeout)
# 保留指定范围内元素
r.ltrim("key", start, stop)
# 增加一个字符串类型数据
r.set("key", "value")
# 增加若干个字符串类型数据
r.mset({"key1": "value1", "key2": "value2", ...})
# 获取一个字符串类型数据
r.get("key")
# 获取若干个字符串类型数据
r.mget("key1", "key2", ...)
# 获取字符串类型数据的长度
r.strlen("key")
# 字符串数据类型增加1
r.incr("key", 1)
# 字符串数据类型减少1
r.decr("key", 1)
# 字符串数据类型增加number，整型
r.incrby("key", number)
# 字符串数据类型减少number，整型
r.decrby("key", number)
# 字符串数据类型增加number，浮点型
r.incrby("key", number)
# 字符串数据类型减少number，浮点型
r.decrby("key", number)
# 增加一条散列数据
r.hset("key", "field", "value")
# 读取散列数据的一条指定字段的值，返回字节串类型
r.hget("key", "field")
# 增加若干散列数据
r.hmset("key", {"field1": "value1", "field2": "value2", ...})
# 读取散列数据的若干指定字段的值
r.hmget("key", "field1", "field2", ...) # 返回结构为[b'value1', b'value2', ...]
# 读取散列数据的所有字段和其对应的值
r.hgetall("key") # 返回结构为{b'field1': b'value1', b'field2': b'value2', ...}
# 读取散列数据的所有字段
r.hkeys("key") # 返回结构为[b'field1', b'field2', ...]
# 读取散列数据的所有值
r.hvals("key")  # 返回结构为[b'value1', b'value2', ...]
# 删除散列数据的指定字段
r.hdel(key, "field1", "field2", ...)
# 集合新增
r.sadd("key", "member1", "member2", ...)
# 集合查看成员
r.smembers("key")
# 集合查看成员个数
r.scard("key")
# 集合查看成员是否存在
r.sismember("key", "member")
# 集合交集
r.sinter("key1", "key2", ...)
# 集合并集
r.sunion("key1", "key2", ...)
# 有序集合添加
r.zadd("key", {"member1": score1, "member2": score2, ...})
# 有序集合分值增加
r.zincrby("key", score, "member")
# 查看排名
r.zrevrange("key", start, stop, [withscores=True|False]) # 返回的结构为[(b'member', score), ...] | [b'member', ...]
# 取并集
r.zunionstore("key", ("key1", "key2", ...), aggregate="max")
# 获取锁或阻塞等待获取锁
with r.lock():
    pass
```