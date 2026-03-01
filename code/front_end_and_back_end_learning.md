# 前后端分离互通项目学习

## 定义

1. 前端：即客户端，负责渲染用户显示画面
2. 后端：即服务器，负责接收http请求处理数据

## 部分名词解析

1. API：Application Programming Interface，是一些预先定义的函数，或指软件系统不同组成部分衔接的约定

## 前后端分离，完整请求过程

### 文解

1. 前端通过http请求后端API
2. 后端以json形式返回前端数据
3. 前端生成用户显示界面

### 图解

![图片]()

## 是否判断标准（基于谁生成页面）

1. 后端生成，即前后端未分离
2. 前端生成，即前后端分离

## 优势

1. 各司其职
   1. 前端：视觉层面，兼容性，前端性能优化
   2. 后端：业务逻辑，并发（可承载的访问数），可用性（nginx的负载均衡），性能（综合）
2. 解耦，易扩展
3. 后端灵活搭配各类前端（iOS，Android，html，...）
4. 提高用户体验
5. 前后端可完全并行开发，加快开发效率

## 分离常见问题

1. 解决http无状态
   * 使用token
2. 前端使用js，解决跨域
   * 使用cors
3. 解决csrf问题
   * 采用token
4. Single Page Web Application对seo（Search Engine Optimization）效果的影响
   * 由于前后端分离后，页面不存在静态文字，会降低seo效率
5. 前后端数据校验
   * 前后端各做一遍，尤其是后端，必须做好数据库前的最后一道防线
6. 动静分离与前后端分离的区别
   * 动静分离：静态资源与服务器分开部署（典型方案，将静态资源交由CDN厂商处理）
   * 前后端分离：页面由前端生成

## token —— 令牌

### 前置知识

#### base64算法

##### 加密方法

1. 将字符串拆成每三个字符一组
2. 计算每一个字符对于的ascii码二进制
3. 将8位的二进制码，按照没6位重新分组，不足6位的在后面补0

##### python库方法（base64）

|方法|作用|参数|
|:----:|:----:|:----:|
|b64encode|将输入的参数转化为base64规则的串|预加密的明文，类型为bytes|
|b64decode|将base64串解密为明文|base64密文，类型为bytes|
|urlsafe_b64encode|作用同b64encode但是会将'+'替换成'-'，将'/'替换成'_'|同b64encode|
|urlsafe_b64decode|作用同b64decode，但只针对上一个方法的解密|同b64decode|

注：base64算法可逆，故可简单的被直接解析

#### 散列算法（hash）

##### 特点

1. 定长输出
2. 不可逆
3. 雪崩

##### 实例

1. SHA-256（安全散列算法的一种，基于hash）
   * 示例

     ```python

     import hashlib
     s = hashlib.sha256()
     s.update(b'xxx')
     s.digest()
     s.hexdigest()
     print(s)

     ```  

2. RSA256（一种非对称加密）
   1. 加密：公钥加密，私钥解密
   2. 签名：私钥签名，公钥验签  
3. python字典与set存储原理（老版本）
   1. 增加
      1. 对键做一次hash，经过一系列操作，得到对应的索引
      2. 当发生哈希碰撞时，会进行二次哈希，再经过一系列操作，得到对应的索引
   2. 删除
      1. 做一次哈希，如果key值相同，作伪删除
      2. 做一次哈希，发现key值不同，做二次哈希，直到键相同，作伪删除
   3. 扩容
      当空闲位置少于三分之一，扩容并重排位置（所以少用字典）

    注：故老版本字典与set都是无序的

4. python字典存储原理更新优化（新版本）
   1. 增加
      1. 对键做一次hash，经过一系列操作，得到对应的索引，此时在另一个辅助列表的对应ha的索引处按顺序存入在实际存储值的列表的索引
      2. 当发生哈希碰撞时，会进行二次哈希，再经过一系列操作，得到对应的索引，同上操作  

   注：故新版本python字典有序  

##### python库

1. hashlib（包含大量基于hash的算法加密库，使用如上示例所示）
2. hmac（包含大量基于hash的算法加密方法，并复合密钥作为盐进行加密的加密库）
   1. 使用示例

      ```python

      # 生成hmac对象
      # 第一个参数为加密的key串，即加盐的内容，bytes类型
      # 第二个参数为欲加密的串，bytes类型
      # 第三个参数为hmac的算法 

      h = hmac.new(key, b'XXX', digestmod='SHA256')
      h.digest()

      ```

##### CMD5

国内通过大量碰撞得到的一个密文反向解密，本质是一个密文与明文的一一映射表

### JWT - json-web-token

#### 组成

1. header
   * 格式：```{'alg': 'HS256', 'typ': 'JWT'}```
   * 参数：
     * 'alg'：即选择的加密算法
     * 'typ'：即使用JWT生成token
   * 注：一般可以省去头部，由于一般开发时会商定协议，同时其传输数据时占据带宽（如果想使用JWT的库的相关方法的话，则不能省去）
   * 呈现方式：先转成json串，再使用base64加密
2. payload
   * 格式：

    ```python

    payload = {
    # 内部提供的几个可选项，公有声明
    'exp': xxx, # 过期时间，为时间戳（expiration time）
    'iss': xxx, # token的签发者（issuer）
    'aud': xxx, # 指明此token签发面向群体(audience)
    'iat': xxx, # 指明此token的创建时间
    # 自己使用的相关内容，私有声明
    'param': xxx,
    ....,
    }
    ```

   * 注：公有声明中一般只使用第一个，即exp
   * 呈现方式：先转成json串，再使用base64加密

3. signature签名
   * 签名规则（以SHA256为例）
      * hmac.new(key, base64后的header + b'.' + base64后的payload， digestmod='SHA256')  
   * 呈现方式：直接使用base64加密

#### 结果格式

```header.payload.signature # 为bytes类型```

#### pyjwt库

##### 安装

```cmd/shell
pip3 install pyjwt
```

##### 方法

1. ```encode(payload, key, algorithm)```
   
   * payload：同上jwt
   * key：加密需要的盐
   * algorithm：加密算法
   * 返回值：token串，数据类型为bytes

2. ```decode(token, key, algorithm)```

   * token：token串，bytes类型
   * key：解密需要的盐
   * algorithm：解密的算法
   * 返回值：payload

##### 异常

* ```jwt.exceptions.ExpiredSignatureError```：解密时token过期抛出

## CORS(Cross origin resource sharing) —— 跨域资源共享

### 什么是CORS

允许浏览器向跨源（协议 + 域名 + 端口）服务器，发出XMLHttpRequest请求，从而克服了AJAX只能同源使用的限制

### 特点

* 浏览器自动完成（在请求头中加入特殊头或发送特殊请求）
* 服务器需要支持（响应头中需要有特殊头）

### 简单请求（Simple requests）和预检请求（Preflilghted requests）

#### 简单请求

##### 满足条件

* 请求方法如下：GET or HEAD or POST
* 请求头仅包含如下：Accept Accept-Lanauage Content-Lanauage Content-Type
* Content-Type仅能为一下之中的一个：application/x-www-form-urlencoded multipart/form-data text/plain

##### 简单请求发送流程

1. 请求：请求头中携带Origin，该字段表明自己来自哪个域
2. 响应：如果请求头中的Origin在服务器接受范围内，则返回如下头
   |响应头|作用|备注|
   |:----:|:----:|:----:|
   |Access-Control-Allow-Origin|服务器接受的域|必选|
   |Access-Control-Allow-Credentials|是否接受Cookie|可选|
   |Access-Control-Expose-Headers|默认情况下，xhr只能拿到如下响应头：Cache-Control，Content-Lanauage，Content-Type，Expires，Last-Modified；如有需要获取其他自定义头，需在此处指定|可选|
   
   注：如果服务器不接受此域，则响应头中不包含Access-Control-Allow-Origin

#### 预检请求

##### 满足条件

所有非简单请求都是预检请求

##### 预检请求发送流程

1. 请求：OPTIOIN请求发起，携带如下请求头
   |请求头|作用|备注|
   |:----:|:----:|:----:|
   |Origin|表明此请求来自哪个域|必选|
   |Access-Control-Request-Method|此次请求使用的方法|必选|
   |Access-Control-Request-Headers|此次请求使用的头|必选|

2. OPTION接受响应阶段，携带如下响应头

   |响应头|作用|备注|
   |:----:|:----:|:----:|
   |Access-Control-Allow-Origin|服务器接受的域|必选|
   |Access-Control-Allow-Methods|告诉浏览器，服务器接受的跨域请求方法|必选|
   |Access-Control-Allow-Headers|返回所有支持的头部，当request有Access-Control-Request-Headers时，响应头必然回复|必选|
   |Access-Control-Allow-Credentials|是否接受Cookie|可选|
   |Access-Control-Max-Age|OPTION请求缓存时间，单位s|可选|

3. 主请求阶段

   |请求头|作用|备注|
   |:----:|:----:|:----:|
   |Origin|表明此请求来自哪个域|必选|

4. 主请求响应阶段

   |响应头|作用|备注|
   |:----:|:----:|:----:|
   |Access-Control-Allow-Origin|服务器接受的域|必选|

## RESTFful —— Representational State Transfer

### RESTful介绍

#### 资源（Resources）

网络上的一个实体，或者说时网络上的一个具体信息，并且每个资源都有一个独一无二的URL与之对应，获取资源只需直接访问URL即可

#### 表现层（Represtation）

如何去表现资源，即资源的表现形式，如：HTML，xml，JPG，json

#### 状态转化（State Transfer）

访问一个URL即发生了一次客户端和服务端的交互，此次交互将会设计数据和状态的变化。客户端需要通过默写方式出发具体的变化，如：GET，POST，PUT，PATCH，DELETE等

### RESTful特征

1. 每一个URL代表一种资源
2. 客户端和服务端之间传递着资源的某种表现
3. 客户端同路过HTTP的几个动作对资源进行操作即发生状态转化

### RESTful特征的URL设计原则

1. 协议：http/https
2. 域名：https://api.example.com/ or htts://example.com/api/
3. 版本：https://api.example.com/v1/
4. 路径：要避免涉及动词，资源用名词表示，案例如下：
   ```text
   https://api.example/v1/users
   https://api.xeample.com/v1/animals
   ``` 
5. HTTP动词语义
   * GET（SELECT）：从服务器中取出资源（一项或多项）
   * POST（CREATE）：在服务器新建一个资源
   * PUT（UPDATE）：在服务器更新资源（客户端提供改变后的完整资源）
   * PATCH（UPDATE）：子服务器更新资源（客户端提供改变的属性）
   * DELETE（DELETE）：从服务器删除资源

   具体案例如下：
   ```text
   GET /zoos：列出所有动物园
   POST /zoos：新建一个动物园
   GET /zoos/id：获取某个指定动物园的信息
   PUT /zoos/id：更新某个指定动物园的信息（提供该动物园的全部信息）
   PATCH /zoos/id：更新某个指定动物园的信息（提供该动物园的部分信息）
   DELETE /zoos/id：删除某个动物园
   GET /zoos/id/animals：列出某个指定动物园的作用动物
   DELETE /zoos/id/animals/id：删除某个指定动物园的指定动物
   ```

6. 巧用查询字符串

   ```text
   ?limit=10：指定返回记录的数量
   ?offset=10：指定返回记录的开始位置
   ?page=2&per_page=100：指定第几页，以及每页的记录数
   ?sortby=name&order=asc：指定返回结果按照某个属性排列，以及排序顺序
   ?type_id=1：指定筛选条件
   ```

7. 状态码
   
   1. 用HTTP响应码表示此次请求结果，例如
      ```text
      200 ok：服务器成功返回用户请求的数据
      201 CREATED：用户新建或修改数据成功
      202 Accepted：表示一个请求已进入后台排队（异步任务）
      204 NO CONTENT：用户删除数据成功
      400 INVALID REQUEST：用户发出的请求有错误，服务器没有进行新建或修改数据的操作，该操作是幂等的
      401 Unauthorized：表示用户没有授权
      403 Forbidden：表示用户得到了授权，但是访问是被禁止的
      404 NOT FOUND：用户发出的请求针对的时不存在的记录，服务器没有进行操作，该操作时幂等的
      406 Not Acceptable：用户请求的格式不可得
      410 Gone：用户请求的资源被永久删除，且不会再得到
      422 Unprocesable entity：当创建一个对象时，发生一个验证错误
      500 INTERNAL SERVER ERROR：服务器发生错误
      ```
   
   2. 自定义内部code进行响应，返回结构如下：```{"code": 100001, "data": {}, "error": "xxx"}```

8. 返回结果（根据HTTP动作的不同，返回结果的结构也有所不同）
   
   ```text
   GET /users：返回资源对象的列表
   GET /users/item：返回单个资源对象
   POST /users：返回新生成的资源对象
   PUT /users/item：返回完整的资源对象
   PATCH /users/item：返回完整的资源对象
   DELETE /users/item：返回一个空文档
   ```