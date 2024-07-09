# 关于仓库中的文件
```
ZJU-Software-College-Project
|
|-README.assets # 保存着README中插入的图片
|
|-java_perf
| |--SPECjvm2008_data # 保存着运行SPECjvm2008时产生的数据
| |--perf # 保存着运行perf和FlameGraph产生的数据
| |--script # 保存着代码和脚本，以及生产的数据
-
```
因为在上传README之前,我用的是绝对路径插入图片，导致上传后图片会无法加载成功，但是我将图片数据上传上来了，下次我会注意用相对路径的😢

# [如何做性能测试](https://www.vimlinux.com/2016/08/11/Performance/)

首先，这份测试报告里的主要问题如下：

- 用的全是平均值。老实说，平均值是非常不靠谱的。

  我们知道，性能测试时，测试得到的结果数据不总是一样的，而是有高有低的，如果算平均值就会出现这样的情况，假如，**测试了10次，有9次是1ms，而有1次是1s，那么平均数据就是100ms，很明显，这完全不能反应性能测试的情况，也许那1s的请求就是一个不正常的值，是个噪点，应该去掉。**

- 响应时间没有和吞吐量TPS/QPS挂钩。而只是测试了低速率的情况，这是完全错误的

  **为什么响应时间（latency）要和吞吐量（Thoughput）挂钩?**

  系统的性能如果只看吞吐量，不看响应时间是没有意义的。当并发量（吞吐量）上涨的时候，系统会变得越来越不稳定，响应时间的波动也会越来越大，响应时间也会变得越来越慢，而吞吐率也越来越上不去

  包括CPU的使用率情况也会如此。所以，当系统变得不稳定的时候，吞吐量已经没有意义了。吞吐量有意义的时候仅当系统稳定的时候。 

- 响应时间和吞吐量没有和成功率挂钩。

​	**为什么响应时间吞吐量和成功率要挂钩?**

​	如果请求不成功的话，都还做毛的性能测试。

# Assignment 1

##  当前系统信息

> `screenfetch` 是一个用于显示系统信息的 Bash 脚本，它以图形化方式在终端中显示系统信息和硬件统计数据。其输出包括操作系统版本、内核版本、桌面环境、CPU、内存、分辨率等，并带有与当前发行版相关的 ASCII 艺术标志。

![image-20240704171956138](D:\School\研学\学校\浙江大学\项目\README.assets\image-20240704171956138.png)

![image-20240704213042949](D:\School\研学\学校\浙江大学\项目\README.assets\image-20240704213042949.png)

## SpecJvm2008使用

### 参考博客

[SpecJvm2008使用说明](https://www.vimlinux.com/2014/09/15/linux/)

### 介绍

SPECjvm® 2008 基准测试是一套用于测量 Java 运行时环境 (JRE) 性能的套件。它包含多个实际应用程序和基准测试，重点关注核心 Java 功能。

**它反映了硬件处理器和内存子系统的性能，与文件系统I/O和网络I/O关系不大。**

SPEC 还认为 Java 的用户体验很重要，因此该套件包括启动基准测试，并具有一个名为 base 的必需运行类别，必须在不进行任何 JVM 调整的情况下运行该类别才能提高开箱即用的性能。

* 一次操作(An Operation)

  **每次调用基准测试工作负载都是一项操作**。该工具将多次调用基准测试，使其在一次迭代中执行多项操作。

* 一次迭代(An Iteration)

  迭代持续一定时间，默认为 240 秒。

  **在此期间，线束将启动多项操作，前一项操作完成后立即启动一项新操作。**它永远不会中止任何操作，而是等到操作完成后再停止。

  线束预计在迭代内完成至少 5 项操作。迭代的持续时间永远不会少于指定时间，但如果操作耗时过长，则根据预热期的性能会增加迭代时间。

* 热身

  套件包含21个基准测试，其中每个基准测试均包含一个2分钟的热身测试和4分钟的正式测试。

  第一次迭代是预热迭代，默认运行 120 秒。预热迭代的结果不包含在基准测试结果中。要跳过预热，请将预热时间设置为 0。

* 工作负载

  SPECjvm2008 工作负载模拟了各种常见的通用应用程序计算。这些特性反映了该基准测试适用于测量运行 Java 的各种客户端和服务器系统上的基本 Java 性能的目标。

> SPECjvm2008 包含一组工作负载，旨在表示多种常见的计算类型。
>
> 一般来说，工作负载中的算法和操作是实际应用程序的组成部分，包括文本/字符处理、数值计算和按位计算（*例如*媒体处理）。
>
> 每个工作负载都有特定的工作量，因此每个工作负载本身都是一个小基准，其中一些基准还有子基准。

* 基值和峰值

  SPECjvm2008 中有两个运行类别，分别称为 Base 和 Peak，此外还有一个额外的运行类别，称为 Lagom。为了创建合规结果，必须包括 Base 类别中的运行。也可以选择包括 Peak 类别中的运行。

  基本类别显示系统性能，无需对 JVM 进行任何调整，即“开箱即用”的性能。但是，它允许调整操作系统和硬件（包括固件，如 BIOS）。基本类别的限制是，您不能对 JVM 进行任何手动调整，也不能更改运行时间。

  峰值类别显示系统可以实现的性能。可以对 JVM 进行调整以实现最佳性能。

  基础运行和峰值运行通过两次单独调用 SPECjvm2008 基准测试套件完成，最初会产生两个不同的结果。这些结果随后会合并为一个原始文件，以便提交。

* 并行性

  大多数基准测试都是并行运行的，即在不同的线程中同时启动多个操作。从测试工具的角度来看，这些线程是独立工作的，但工作负载的设计会引入一系列有趣的问题，既会在应用程序级别共享数据和工作，也会使用 JVM 内部共享的资源。

* 基准测试亮点
  利用实际应用程序（如 derby、sunflow 和 javac）和以领域为重点的基准测试（如 xml、序列化、加密和 scimark）。
  还测量在执行 JRE 的上下文中操作系统和硬件的性能。

* 结果
  已提交结果 - SPECjvm2008 基准测试指标的文本和 HTML 输出；包括基准测试许可证持有者提交给 SPEC 的所有结果。

上述是[官网](https://www.spec.org/jvm2008/)的内容

<hr>

### 下载specJvm2008：[地址](https://www.spec.org/jvm2008/)


> SPECjvm2008 requires a Java Runtime Environment supporting Java SE 5.0 features.
>
> > 针对不同的开发市场，Sun公司将Java划分为三个技术平台，它们分别是Java SE、JavaEE和Java ME。
> >
> > Java SE(Java Platform Standard Edition,Java 平台标准版)。该版本是为开发普通桌面和商务应用程序提供的解决方案。

```
java -jar SPECjvm2008_1_01_setup.jar -i console
```

```
Product Name:
    SPECjvm2008

Install Folder:
    /home/cilinmengye/java_perf/SPECjvm2008
```

**惨痛教训**

我在配置java的JAVA_HOME和CLASSPATH环境时，我更改的是`.bashrc`,而不是`/etc/profile`

> **用户级配置文件**：`~/.bashrc` 是当前用户的 shell 初始化文件。
>
> **全局配置文件**：`/etc/profile` 是全局配置文件，用于所有用户的 shell 环境初始化。

当安装默认安装到`/SPECjvm2008`下，运行`SPECjvm2008`需要root的权限，这样会在root的PATH下查找，而我只是配置了用户下的PATH

如果没有权限，运行会有如下结果：

一旦运行会导致`Aborting.`出现在屏幕上

```
java -jar SPECjvm2008.jar -wt 5s -it 5s -bt 2 compress
```

![image-20240704164656396](D:\School\研学\学校\浙江大学\项目\README.assets\image-20240704164656396.png)

### 在Linux中使用java和设置环境变量

jdk : java development kit java开发工具包

jre : java runtime environment 运行时环境

jvm : java virtual machine java虚拟机

jdk = jre + java开发工具

jre = jvm + java核心类库

> Oracle JDK 和 OpenJDK 都是被称为 Java 开发套件的一组软件和规范。
>
> 实际上，Oracle JDK 和 OpenJDK 之间几乎没有代码差异，所以它们的功能非常相似。 
>
> OpenJDK 和 Oracle JDK 之间最大的区别在于，OpenJDK 是一个由 Oracle、红帽和社区维护的开源项目，而 Oracle JDK 是闭源的，需要购买付费许可证，并由 Oracle 维护。

在ubuntu22.04.4中下载**openjdk 8**

1. Ensure the `apt` libraries are updated.

   ```bash
   sudo apt update && sudo apt upgrade -y
   ```

2. [Install OpenJDK](https://docs.datastax.com/en/jdk-install/doc/jdk-install/installOpenJdkDeb.html):

   ```bash
   sudo apt-get install openjdk-8-jdk
   ```

   ```
   cilinmengye@cilinmengye:~$ java -version
   openjdk version "1.8.0_412"
   OpenJDK Runtime Environment (build 1.8.0_412-8u412-ga-1~22.04.1-b08)
   OpenJDK 64-Bit Server VM (build 25.412-b08, mixed mode)
   ```

   ![image-20240705165155836](D:\School\研学\学校\浙江大学\项目\README.assets\image-20240705165155836.png)

3. [set java environment](https://www.cnblogs.com/FengZeng666/p/12580401.html)

   ```
   cd ~/
   vim ./.bashrc
   export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
   export CLASSPATH=.:${JAVA_HOME}/lib/tools.jar:${JAVA_HOME}/lib/dt.jar
   export PATH=$JAVA_HOME/bin:$PATH
   :wq
   ```

## 阅读文档

### FQA

1. Q1.4：SPECjvm2008 中是否包含所有源代码？

   是的，所有源代码都已包含，可供查看和分析。组件根据不同的许可证提供，请参阅许可证文件。

2. Q1.6：SPECjvm2008 测试什么？

   SPECjvm2008 旨在测试 JRE 在典型 Java 应用程序上的性能，包括 Java 库（如 JAXP (XML) 和 Crypto），这两种工作负载对于客户端和服务器端 Java 应用程序来说都很常见。其他因素包括应用程序环境，例如硬件和操作系统。有关具体测试内容的更多信息，请参阅每个基准的基准文档。

3. Q1.8：SPECjvm2008 中的一个基准测试需要运行多长时间？

   一个基准测试的预热时间为 2 分钟，测量运行时间为 4 分钟。**在此期间，将执行多项操作。操作永远不会中断，因此所有线程将继续运行，直到所有线程完成在测量间隔内启动的操作。**

4. Q1.11：SPECjvm2008 中**操作长度以秒为单位**的原因是什么？

5. Q2.1：SPECjvm2008 的性能指标是什么？

   SPECjvm2008 生成以下**以每分钟操作次数 (ops/m) 为单位的吞吐量指标**：

   * 总基础吞吐量测量（SPECjvm2008 Base ops/m）
     这是从一次完全合规的基础运行中获得的总体吞吐量结果。基础运行要求 JVM 不进行任何手动调优。
   * 总峰值吞吐量测量（SPECjvm2008 Peak ops/m）
     这是从一次完全合规的峰值运行中获得的总体吞吐量结果。峰值运行允许对 JVM 进行调优，代表系统能够达到的最大吞吐量。

   > Q2.1: What is the performance metric for SPECjvm2008?
   >
   > SPECjvm2008 produces these throughput metrics in operations per minute (ops/m):
   >
   > The total base throughput measurement, SPECjvm2008 Base ops/m
   > This is the overall throughput result obtained from a full compliant base run. A base run requires that there is no hand tuning of the JVM.
   > The total peak throughput measurement, SPECjvm2008 Peak ops/m
   > This is the overall throughput result obtained from a full compliant peak run. A peak run does allow tuning of the JVM and represent the maximum throughput that can be achieved with the system.

6. Q4.2：为什么我的运行时间超过了 20 秒，即使我在命令行中指定了 10 秒？

   子基准测试中的一个操作尚未完成，且 SPECjvm2008 不允许中断操作。参见问题 Q1.10 了解其中的原因。

   这也可能是由于预热阶段的结果表明迭代时间不足以完成五次操作。因此迭代时间将会增加。如果发生这种情况，框架会打印一条消息。如果一次运行未能至少完成 5 次操作，则认为该运行时间过短。

7. Q4.3：如果出现 OutOfMemoryError，我该怎么办？

   可能会抛出内存不足错误。是否以及何时发生这种情况取决于所使用的 JVM 及其运行平台，特别是逻辑 CPU 的数量。

   抛出该错误是因为基准测试中的实时数据量大于 JVM 可以容纳在堆中的量。

   实时数据量随着基准测试线程数的增加而增加，因此机器越大，发生这种情况的可能性就越大。

   [请参阅有关 OOME 的已知问题文档，了解更多信息和推荐的解决方法。](file:///SPECjvm2008/docs/KnownIssues.html#OutOfMemory)

8. **Q4.8：为什么 SPECjvm2008 不能在 Java SE 8、Java SE 9 或更高版本上运行？**

   Java SE 8 及以后的规范不受支持。参见故障排除，问题 Q3.2。

   > Q3.2：运行基准测试需要什么软件？
   >
   > SPECjvm2008 需要 Java 运行时环境，该环境支持 Java SE 1.5.0、Java SE 6 或 Java SE 7 规范中定义的此基准测试引用的类的完整实现。不支持其他 Java SE 规范（如 SPECjvm2008 运行规则第 2.1 节中所述）。
   >
   > 您可以尝试使用 JDK-8 或更高版本运行，但我们不提供任何保证。请参阅故障排除，Q4.8。

   **对于 Java SE 8 及以后的版本**：

   以下 SPECjvm2008 基准测试已知无法运行：

   - startup.compiler.compiler
   - startup.compiler.sunflow
   - compiler.compiler
   - compiler.sunflow

   但是，你可以通过命令行或使用属性文件，指定所有的基准测试（除了上述的）来运行剩余的基准测试。有关如何操作的信息，请参见：

   - http://www.spec.org/jvm2008/docs/UserGuide.html#OperationalConfiguration
   - http://www.spec.org/jvm2008/docs/UserGuide.html#Properties
   - http://www.spec.org/jvm2008/docs/UserGuide.html#AppendixA
   - http://www.spec.org/jvm2008/docs/UserGuide.html#SPECjvm2008WorkloadNames

### [SPECjvm2008 Known Issues](https://www.spec.org/jvm2008/docs/KnownIssues.html)

    1. Out of Memory Error
    2. Validation failure in XML transform benchmark
    3. Null Pointer Exception in XML validation benchmark
    4. Check test failure using Java for Mac OS X
    5. Build error with Java for Mac OS X
    6. Unable to run with SoyLatte JVM on Mac OS X (10.4), need X11
    7. Crash of JVM in pkcs11_softtoken.so running on Solaris 10.4

### Benchmark Name Description

```
startup.helloworld  测试helloworld程序从运行开始到结束所需的时间
startup.compiler.compiler   普通java编译所需要的时间
startup.compiler.sunflow    编译sunflow图像渲染引擎所需要的时间
startup.compress    测试压缩程序，单次压缩所需的时间
startup.crypto.aes  测试AES/DES加密算法，单次加解密所需的时间
输入数据长度为 100 bytes , 713KB
startup.crypto.rsa  测试RSA加密算法，单次加解密需要的时间
输入数据长度为 100 bytes, 16KB 
startup.crypto.signverify   测试单次使用MD5withRSA, SHA1withRSA, SHA1withDSA, SHA256withRSA来签名，识别所需要的时间。
输入数据长度为 1KB, 65KB, 1MB
startup.mpegaudio   单次mpeg音频解码所需的时间
startup.scimark.fft 单次快速傅立叶变换所需的时间
startup.scimark.lu  单次LU分解所需的时间
startup.scimark.monte_carlo 单次运行蒙特卡罗算法所需的时间
startup.scimark.sor 单次运行jacobi逐次超松弛迭代法所需的时间
startup.scimark.sparse  单次稀疏矩阵乘积所需的时间
startup.serial  单次通过socket传输java序列化对象到对端反序列化完成所需的时间（基于jboss serialization benchmark）
startup.sunflow 单次图片渲染处理所需的时间
startup.xml.transform   单次xml转换所需的时间，转换包括dom,sax,stream方式
startup.xml.validation  单次xml schema校验所需的时间
compiler.compiler   在规定时间内，多线程迭代测试普通java编译，得出 ops/m
compiler.sunflow    在规定时间内，多线程迭代测试sunflow图像渲染，得出 ops/m
compress    在规定时间内，多线程迭代测试压缩，得出 ops/m
crypto.aes  在规定时间内，多线程迭代测试AES/DES加解密算法，得出 ops/m
crypto.rsa  在规定时间内，多线程迭代测试RSA加解密算法，得出 ops/m
crypto.signverify   在规定时间内，多线程迭代测试使用MD5withRSA, SHA1withRSA, SHA1withDSA, SHA256withRSA来签名，识别，得出 ops/m
derby   在规定时间内，迭代测试数据库相关逻辑，包括数据库锁，BigDecimal计算等，最后得出 ops/m
mpegaudio   在规定时间内，多线程迭代mpeg音频解码，得出 ops/m
scimark.fft.large   在规定时间内，多线程迭代测试快速傅立叶变换，使用32M大数据集，最后得出 ops/m
scimark.lu.large    在规定时间内，多线程迭代测试LU分解，使用32M大数据集，最后得出 ops/m
scimark.sor.large   在规定时间内，多线程迭代测试jacobi逐次超松弛迭代法，使用32M大数据集，最后得出 ops/m
scimark.sparse.large    在规定时间内，多线程迭代测试稀疏矩阵乘积，使用32M大数据集，最后得出 ops/m
scimark.fft.small   在规定时间内，多线程迭代测试快速傅立叶变换，使用512K小数据集，最后得出 ops/m
scimark.lu.small    在规定时间内，多线程迭代测试LU分解，使用512KB小数据集，最后得出 ops/m
scimark.sor.small   在规定时间内，多线程迭代测试jacobi逐次超松弛迭代法，使用512KB小数据集，最后得出 ops/m
scimark.sparse.small    在规定时间内，多线程迭代测试稀疏矩阵乘积，使用512KB小数据集，最后得出 ops/m
scimark.monte_carlo 在规定时间内，多线程迭代测试蒙特卡罗算法，得出 ops/m
serial  在规定时间内，多线程迭代测试通过socket传输java序列化对象到对端反序列化（基于jboss serialization benchmark），得出 ops/m
sunflow 在规定时间内，利用sunflow多线程迭代测试图片渲染，得出 ops/m
xml.transform   在规定时间内，多线程迭代测试xml转换，得出ops/m
xml.validation  在规定时间内，多线程迭代测试xml schema验证，得出 ops/m
```

## 运行specjvm2008

### [Trial run](https://www.spec.org/jvm2008/docs/UserGuide.html#TrialRun)

```
java -jar SPECjvm2008.jar -wt 5s -it 5s -bt 2 compress
```

按照官方文档上的说明进行试运行，这条命令会启动 SPECjvm2008 工具并运行 `compress` 基准测试，使用以下配置：

- -wt: 在实际测试之前进行 5 秒的预热。
- -it: 实际测试中每次迭代运行 5 秒。
- -bt: 使用 2 个线程并行运行 `compress` 基准测试。

![image-20240705104750358](D:\School\研学\学校\浙江大学\项目\README.assets\image-20240705104750358.png)

### 运行

运行基准测试的命令行的一般形式是

```
java [<jvm 选项>] -jar SPECjvm2008.jar [<SPECjvm2008 选项>] [<基准名称> ...]
```

> 要运行基本类别，请在命令行上指定 --base。除非使用 JVM 命令行参数或更改运行时，否则此类别为默认类别。
>
> 要运行峰值类别，请在命令行上指定 --peak。如果使用 JVM 命令行参数或更改运行时，也会自动选择此选项。

或者可以使用如：`./run-specjvm.sh startup.helloworld -ikv` 

SPECjvm2008 在运行时将其操作记录打印到标准输出流。它可选择生成一个 XML 文件，该文件记录用户提供的**系统信息、一些参数值和运行结果。**

XML 文件将写入名为`RESULTS_DIR/SPECjvm2008.<数字>/SPECjvm2008<数字>.raw`

XML 文件的写入位置由参数 的值控制`specjvm.result.dir`；默认值是当前工作目录中名为“results”的子目录。

#### 吞吐量

在给定的运行中，每个 SPECjvm2008 子基准测试都会产生一个以 **ops/min（每分钟操作数）**为单位的结果，该结果反映了系统能够完成该子基准测试工作负载调用的速率。

在运行结束时，SPECjvm2008 会计算一个数量，旨在反映系统在运行期间执行的所有子基准测试上的整体性能。计算组合结果的基本方法是**计算几何平均值**。

> 几何平均值是通过对一组正数的乘积开其 n 次方根来计算的，其中 n 是数据点的数量。
>
> 对于一组正数$ x1,x2,…,x_n$，几何平均值 G 计算公式为：
>
> $G= \sqrt[n]{x_1 \times x_2 \times \cdots \times x_n}$

虽然仅执行选定子基准测试的运行所获得的吞吐量结果可能很有趣，并且对研究目的很有用，但只有**执行所有子基准测试（并满足其他几个条件）的运行所获得的整体吞吐量结果**才被认为代表系统在 SPECjvm2008 上的性能。

#### 结果报告

单次运行的基准测试结果报告将写入如上所述的单个结果目录中[。](https://www.spec.org/jvm2008/docs/UserGuide.html#Output and Results - Location)结果文件包括以下部分或全部内容。

* SPECjvm2008.<编号>.raw
* SPECjvm2008.<编号>.html
* SPECjvm2008.<编号>.txt
* SPECjvm2008.<编号>.sub
* SPECjvm2008.<编号>.摘要

如果 HTML 结果文件存在，还会有一个*图像* 子目录，其中包含 HTML 结果文件引用的 .jpg 文件。

> HTML 和文本报告是根据 XML 结果文件生成的，主要供人类查看。它们都包含基本相同的信息。

#### HelloWorld

```
./run-specjvm.sh startup.helloworld -ikv
```

使用基准测试目录下提供的`run-specjvm.sh`脚本以启动测试序列。

![image-20240705104941851](D:\School\研学\学校\浙江大学\项目\README.assets\image-20240705104941851.png)

#### Full Run

官方文档已经指出Java8不支持4个测试项，于是手动指定了其余的测试项，排除的测试项分别是

- startup.compiler.compiler
- startup.compiler.sunflow
- compiler.sunflow
- compiler.sunflow

执行的脚本如下

```
java -jar SPECjvm2008.jar -i console -ikv startup.helloworld  startup.compress startup.crypto.aes startup.crypto.rsa startup.crypto.signverify startup.mpegaudio startup.scimark.fft startup.scimark.lu startup.scimark.monte_carlo startup.scimark.sor startup.scimark.sparse startup.serial startup.sunflow startup.xml.validation compress crypto.aes crypto.rsa crypto.signverify derby mpegaudio scimark.fft.large scimark.lu.large scimark.sor.large scimark.sparse.large scimark.fft.small scimark.lu.small scimark.sor.small scimark.sparse.small scimark.monte_carlo serial sunflow xml.validation
```

![image-20240705105712341](D:\School\研学\学校\浙江大学\项目\README.assets\image-20240705105712341.png)

![image-20240705105727665](D:\School\研学\学校\浙江大学\项目\README.assets\image-20240705105727665.png)

![image-20240705105823587](D:\School\研学\学校\浙江大学\项目\README.assets\image-20240705105823587.png)

![image-20240705105856193](D:\School\研学\学校\浙江大学\项目\README.assets\image-20240705105856193.png)

![image-20240705110331634](D:\School\研学\学校\浙江大学\项目\README.assets\image-20240705110331634.png)

![image-20240705110939206](D:\School\研学\学校\浙江大学\项目\README.assets\image-20240705110939206.png)

![image-20240705112305936](D:\School\研学\学校\浙江大学\项目\README.assets\image-20240705112305936.png)

> 运行的Benchmark为derby

## Answer to the Assignment 1

###  What is the performance metric of SPECjvm2008? Why? What are the units of measurements?

SPECJvm2008的性能指标是吞吐量，单位是ops/min（每分钟操作数)

使用吞吐量作为单位的原因：

1. 反映系统在高负载下的效率和长时间运行下的稳定性

   吞吐量衡量的是系统在给定时间内完成多少工作。对于一个 JVM，在高负载下能够处理的操作次数直接关系到它的实际使用场景。

   长时间的高负载操作会引发 JVM 内部的一些“副作用”（如垃圾回收、内存分配压力等），使用吞吐量指标可以验证 JVM 在处理这些“副作用”时的稳定性和效率。（官方文档在回答SPECjvm2008 中**操作长度以秒为单位**的原因是什么时提到了这点）

2. 能够评估整体系统性能

   吞吐量作为性能指标，不仅仅评估了 CPU 执行速度，还综合考虑了内存管理、垃圾回收等各个方面的性能。

3. 能够评估多线程和并发处理的能力

   由于现代 Java 应用程序通常在多线程环境下运行，吞吐量能够反映 JVM 在这种环境中处理并发任务的能力，尤其是在处理请求、执行任务等操作时的效率。

### What factors affect the scores? Why some get higher scores, but others get lower scores?

1. 程序的计算复杂度

   ![image-20240705113925502](D:\School\研学\学校\浙江大学\项目\README.assets\image-20240705113925502.png)

   在单线程执行的情况下，测试程序中最简单的`startup.hellworld`得分最高

   对于其他在单线程下执行的测试程序，得分第二高的为`startup.crypto.rsa`

   ![image-20240705114958560](D:\School\研学\学校\浙江大学\项目\README.assets\image-20240705114958560.png)

   但是`startup.hellworld`的得分是`startup.crypto.rsa`的2.5倍！

   涉及复杂算法或数据处理的程序需要更多的 CPU 资源和运行时间，当程序的计算复杂度高时，每个任务所需的计算时间变长，导致单位时间内处理的任务数量减少，从而降低吞吐量。

2. 并行度

   在多线程下多次迭代测试某一程序得分比在单线程下单次测试某一程序得分高的多

   ![image-20240705120013888](D:\School\研学\学校\浙江大学\项目\README.assets\image-20240705120013888.png)

   ![image-20240705120041581](D:\School\研学\学校\浙江大学\项目\README.assets\image-20240705120041581.png)

   如上图：

   ```
   startup.crypto.aes  测试AES/DES加密算法，单次加解密所需的时间
   输入数据长度为 100 bytes , 713KB
   startup.crypto.rsa  测试RSA加密算法，单次加解密需要的时间
   输入数据长度为 100 bytes, 16KB 
   ```

   crypto.aes  在规定时间内，多线程迭代测试AES/DES加解密算法，得出 ops/m
   crypto.rsa  在规定时间内，多线程迭代测试RSA加解密算法，得出 ops/m

    可以有效利用多核 CPU 资源的程序，减少单个任务的执行时间，其吞吐量较高。

3. 是否进行了热身

   ![image-20240705115723437](D:\School\研学\学校\浙江大学\项目\README.assets\image-20240705115723437.png)

   在经过热身后，热身后进行迭代程序的得分要比热身时得分要高一点

   影响原因会在下一个问题中回答

4. 对内存和缓存的使用方式

   ```
   scimark.fft.large   在规定时间内，多线程迭代测试快速傅立叶变换，使用32M大数据集，最后得出 ops/m
   scimark.lu.large    在规定时间内，多线程迭代测试LU分解，使用32M大数据集，最后得出 ops/m
   scimark.sor.large   在规定时间内，多线程迭代测试jacobi逐次超松弛迭代法，使用32M大数据集，最后得出 ops/m
   scimark.sparse.large    在规定时间内，多线程迭代测试稀疏矩阵乘积，使用32M大数据集，最后得出 ops/m
   ```

   ![image-20240705121017825](D:\School\研学\学校\浙江大学\项目\README.assets\image-20240705121017825.png)

   ![image-20240705121032519](D:\School\研学\学校\浙江大学\项目\README.assets\image-20240705121032519.png)

   ```
   scimark.fft.small   在规定时间内，多线程迭代测试快速傅立叶变换，使用512K小数据集，最后得出 ops/m
   scimark.lu.small    在规定时间内，多线程迭代测试LU分解，使用512KB小数据集，最后得出 ops/m
   scimark.sor.small   在规定时间内，多线程迭代测试jacobi逐次超松弛迭代法，使用512KB小数据集，最后得出 ops/m
   scimark.sparse.small    在规定时间内，多线程迭代测试稀疏矩阵乘积，使用512KB小数据集，最后得出 ops/m
   ```

   ![image-20240705121106966](D:\School\研学\学校\浙江大学\项目\README.assets\image-20240705121106966.png)

   ![image-20240705122715898](D:\School\研学\学校\浙江大学\项目\README.assets\image-20240705122715898.png)

可以看到在小数据集上运行明显比在大数据集上运行得分更高

这是可能是因为：

1. 频繁分配和访问大块内存的程序可能会触发**频繁的垃圾回收**，从而降低性能。
2. 频繁进行大数据集访问的程序可能由于**缓存失效**而得分较低，而一个主要在小数据集上操作的程序可能得分较高。

### Why is warmup required in SPECjvm2008, and does warmup time have any impact on performance test results?

**热身** 主要为了让 JVM 达到稳定的性能状态，使得在正式性能测试期间得到的结果更加可靠和准确。

**(1) 提高 JVM 效率**

- **即时编译（JIT）**: 热身期间，JVM 的即时编译器会将热点字节码转换为高效的本地机器码，减少解释执行的开销。
- **优化**: JVM 会在热身时对代码进行优化，例如方法内联和循环展开，从而提升程序执行效率。

**(2) 稳定内存使用**

- **内存分配**: 在热身期间，JVM 会为程序分配所需的内存区域，并进行必要的初始化。
- **垃圾回收**: 热身可以触发垃圾回收，使 JVM 调整堆内存布局，减少在正式测试期间的内存碎片和频繁 GC 影响。

**(3) 缓存填充**

- **类加载缓存**: 热身期间会加载和链接所有必需的类，使其在正式测试期间不会再产生类加载开销。
- **数据缓存**: 热身可以填充 CPU 和内存缓存，提高数据访问的局部性，从而提升性能。

**1. 稳定测试环境**

- **消除初始启动开销**：在 JVM 上运行的应用程序，特别是需要大量计算或涉及频繁内存操作的应用，通常会在刚启动时经历一段不稳定期。这期间，JVM 可能会进行一些初始化操作，如类加载、JIT（Just-In-Time）编译等。预热期的作用是让这些初始化操作完成，从而使得后续的性能测量不受初始启动开销的影响。
- **达到运行状态**：应用程序在启动后会逐渐进入稳定的运行状态。在这段时间内，JVM 会对代码进行优化，JIT 编译会将热路径编译为本地代码，缓存数据也会填充等。这些都会导致初始运行时的性能不稳定。预热期让程序运行一段时间，达到稳定状态后再进行性能测试，从而得到更准确的结果。

**2. 调整迭代时间**

- **确保完成足够的操作**：如果在预热期间发现单次迭代的时间不足以完成预期的操作次数（例如不足以完成五次操作），基准测试可能会调整迭代时间。这是为了保证每次迭代都能进行足够的操作，使得测试结果具有统计意义，并能够全面反映系统性能。

  在 SPECjvm2008 中，预热期不仅帮助测试环境达到稳定状态，还能根据实际运行状况调整迭代时间。例如，如果初始设置的迭代时间不足以完成五次操作，预热期的结果会显示这种情况，并导致测试系统自动增加迭代时间，以确保每次迭代能够完成足够的操作，从而使得测试结果更具代表性。

  <hr>

- **稳定环境**：通过消除初始启动的各种开销，确保测试环境达到稳定状态。

- **迭代时间调整**：通过预热期间的反馈，调整迭代时间以确保每次迭代能够完成足够的操作次数，从而使得性能测量准确可靠。

  <hr>

**热身时间** 对测试结果有显著影响，因为它决定了 JVM 在正式测试开始时的状态。具体影响如下：

**(1) 热身时间不足**

- **未完成编译和优化**: 如果热身时间太短，JIT 编译和优化可能未完成，导致程序仍在以解释模式运行，从而性能较差。
- **内存未稳定**: 短暂的热身可能导致内存布局未稳定，正式测试期间可能会有更多的 GC 开销。
- **缓存未填充**: 不足的热身时间可能导致数据未能充分缓存，增加数据访问延迟。

**(2) 过长的热身时间**

- **浪费资源**: 过长的热身时间可能导致资源浪费，延长了整个测试周期。
- **潜在过度优化**: 极端情况下，过长的热身时间可能导致 JVM 进行一些非常规优化，影响测试的通用性。

**(3) 合适的热身时间**

- **充分优化和稳定**: 合适的热身时间能确保 JVM 完成必要的编译、优化和内存调整，使测试期间 JVM 达到稳定状态。
- **提高结果准确性**: 使得测试结果更能反映程序在生产环境中的实际性能。

### Did you get close to 100% CPU utilization running SPECjvm2008? Why or why not?

在开始时，CPU利用率还未接近100%，但是利用率在逐步上升

在运行一段时间后，CPU利用率长时间接近100%。

这是因为

**工作负载特性**:SPECjvm2008 包含了许多 CPU 密集型的基准测试，例如压缩、加密操作以及科学计算。像 `compress` 和 `crypto` 这样的基准测试，需要进行大量计算和数据转换，能使 CPU 饱和。

**持续执行**: 基准测试会连续运行较长时间，保持稳定的工作负载，使 CPU 保持繁忙状态。

**迭代与重复**: 许多基准测试会反复执行相同的任务，从而帮助驱动 CPU 达到其最大容量。

**多线程**: 在后续测试中，SPECjvm2008 包括使用多个 CPU 核心，以多线程方式运行的测试。

# Assignment 2

## 各个JDK版本安装和环境设置

openJDK `/usr/lib/jvm/java-8-openjdk-amd64/bin/java`

<hr>


[阿里巴巴 Dragonwell](https://dragonwell-jdk.io/#/index)`/usr/lib/jvm/dragonwell-8.19.20/bin/java`

```
cd /usr/lib/jvm

sudo wget https://dragonwell.oss-cn-shanghai.aliyuncs.com/8.19.20/Alibaba_Dragonwell_Extended_8.19.20_x64_linux.tar.gz

sudo tar xzvf Alibaba_Dragonwell_Extended_8.19.20_x64_linux.tar.gz

sudo update-alternatives --install /usr/bin/java java /usr/lib/jvm/dragonwell-8.19.20/bin/java 2

sudo update-alternatives --install /usr/bin/javac javac /usr/lib/jvm/dragonwell-8.19.20/bin/javac 2
```

![image-20240705152813932](D:\School\研学\学校\浙江大学\项目\README.assets\image-20240705152813932.png)

<hr>


[Tencent Kona v8.0.18-GA](https://github.com/Tencent/TencentKona-8/releases/tag/8.0.18-GA)`/usr/lib/jvm/dragonwell-8.19.20/bin/java`

```
sudo wget https://github.com/Tencent/TencentKona-8/releases/download/8.0.18-GA/TencentKona8.0.18.b1_jdk_linux-x86_64_8u412.tar.gz

sudo tar xzvf TencentKona8.0.18.b1_jdk_linux-x86_64_8u412.tar.gz

sudo update-alternatives --install /usr/bin/java java /usr/lib/jvm/TencentKona-8.0.18-412/bin/java 2

sudo update-alternatives --install /usr/bin/javac javac /usr/lib/jvm/TencentKona-8.0.18-412/bin/javac 2
```

![image-20240705154142536](D:\School\研学\学校\浙江大学\项目\README.assets\image-20240705154142536.png)

<hr>


[华为 Bisheng](https://gitee.com/openeuler/bishengjdk-8/wikis/%E6%AF%95%E6%98%87JDK%208%20%E5%AE%89%E8%A3%85%E6%8C%87%E5%8D%97?sort_id=2891179)

```
sudo wget https://mirrors.huaweicloud.com/kunpeng/archive/compiler/bisheng_jdk/bisheng-jdk-8u412-linux-x64.tar.gz

sudo tar xzvf bisheng-jdk-8u412-linux-x64.tar.gz

sudo update-alternatives --install /usr/bin/java java /usr/lib/jvm/bisheng-jdk1.8.0_412/bin/java 2

sudo update-alternatives --install /usr/bin/javac javac /usr/lib/jvm/bisheng-jdk1.8.0_412/bin/javac 2
```

![image-20240705155505108](D:\School\研学\学校\浙江大学\项目\README.assets\image-20240705155505108.png)

<hr>


[Linux 如何查看jdk安装路径](https://www.cnblogs.com/kerrycode/p/4762921.html)

> **`java` 命令** 用于运行 Java 程序。它启动 Java 虚拟机（JVM），加载指定的类，并执行 `main` 方法。
>
> **`javac` 命令** 是 Java 编译器，用于将 Java 源代码（`.java` 文件）编译成字节码（`.class` 文件）。

### JDK版本管理

```
sudo update-alternatives --config java //切换java命令版本
sudo update-alternatives --config javac //切换javac命令版本
```

## 工作负载选择和配置

配置调整：找不到每个供应商对所选工作负载进行优化的建议...

SPECJvm2008 工具在调整工作负载以便尽可能有效地与基准测试配合使用方面非常灵活。

SPECjvm2008 的完整参数集记录在附录 A 以及文件 props/specjvm.properties 和 props/specjvm.reporter.properties 中。

## 基准测试

workload：compress

```
# openjdk
/usr/lib/jvm/java-8-openjdk-amd64/bin/java -jar SPECjvm2008.jar -ikv compress
# 阿里巴巴 Dragonwell
/usr/lib/jvm/dragonwell-8.19.20/bin/java -jar SPECjvm2008.jar -ikv compress
# Tencent Kona
/usr/lib/jvm/TencentKona-8.0.18-412/bin/java -jar SPECjvm2008.jar -ikv compress
# 华为 Bisheng
/usr/lib/jvm/bisheng-jdk1.8.0_412/bin/java -jar SPECjvm2008.jar -ikv compress
```

![image-20240705170911674](D:\School\研学\学校\浙江大学\项目\README.assets\image-20240705170911674.png)

> openjdk 
>
> warmup: 166.18ops/m 
>
> composite: 162.73ops/m

![image-20240705180716507](D:\School\研学\学校\浙江大学\项目\README.assets\image-20240705180716507.png)

> Dragonwell
>
> warmup: 160.23ops/m 
>
> composite: 152.97ops/m

![image-20240705181548692](D:\School\研学\学校\浙江大学\项目\README.assets\image-20240705181548692.png)

> Kona
>
> warmup: 157.18ops/m 
>
> composite: 156.60ops/m

![image-20240705182443969](D:\School\研学\学校\浙江大学\项目\README.assets\image-20240705182443969.png)

> Bisheng
>
> warmup: 162.57ops/m 
>
> composite: 158.72ops/m

感觉运行多次的效率实在是太低了...我要写个sh脚本

```sh
#!/usr/bin/bash

# 注意：数组定义时，元素之间不能有逗号
commands=("/usr/lib/jvm/java-8-openjdk-amd64/bin/java -jar SPECjvm2008.jar -ikv compress" "/usr/lib/jvm/dragonwell-8.19.20/bin/java -jar SPECjvm2008.jar -ikv compress"
	  "/usr/lib/jvm/TencentKona-8.0.18-412/bin/java -jar SPECjvm2008.jar -ikv compress" "/usr/lib/jvm/bisheng-jdk1.8.0_412/bin/java -jar SPECjvm2008.jar -ikv compress")

jdks=("openjdk" "dragonwell" "kona" "bisheng")

touch "tmp"
touch "info"
cd ../SPECjvm2008 || exit 1
tmp_path="../script/tmp"
info_path="../script/info"
len=${#commands[@]}

for ((i = 1; i <= 6; i++)); do
    for ((j = 0; j < $len; j++)); do
        # 执行命令并用正则表达式识别结果并存储在文件中
        eval "${commands[j]}" > "$tmp_path"
        line=$(grep "Noncompliant composite result:" "$tmp_path")
        result=$(echo "$line" | awk -F'[ :]+' '{print $4}')
	
	cat "$tmp_path" >> "$info_path"
	echo "${jdks[j]}_${i}: $result\n"

        if [ -e "../script/${jdks[j]}" ]; then
            echo "$result" >> "../script/${jdks[j]}"
        else 
            touch "../script/${jdks[j]}"
            echo "$result" >> "../script/${jdks[j]}"
        fi

        # 进入results文件夹并修改报告名称
        cd ./results || exit 1
        mv SPECjvm2008.001 "${jdks[j]}_$i" 2>/dev/null
        cd ..
    done
done

rm '$tmp_path'

```

每一个测试包括2分钟热身，4分迭代，总共6分钟.

考虑到时间上的成本，我对每个jdk进行6次测试

我sh脚本总共运行时间为：$6 * 4 * 6 = 144m = 2.4h$

得到如下结果：

```python
scores =  {
	'openjdk': [158.67, 155.67, 157.48, 164.16, 158.79, 159.2],
    'dragonwell': [157.55, 160.77, 159.32, 164.34, 157.42, 160.06]，
    'kona': [159.39, 156.13, 163.72, 161.39, 161.01, 156.9],
    'bisheng'： [156.79, 157.14, 159.55, 153.87, 160.12, 152.38]
}
```

## 数据分析

| JDK        | round 1 | round 2 | round 3 | round 4 | round 5 | round6 | mean   | std  |
| ---------- | ------- | ------- | ------- | ------- | ------- | ------ | ------ | ---- |
| openjdk    | 158.67  | 155.67  | 157.48  | 164.16  | 158.79  | 159.2  | 158.99 | 2.83 |
| dragonwell | 157.55  | 160.77  | 159.32  | 164.34  | 157.42  | 160.06 | 159.91 | 2.54 |
| kona       | 159.39  | 156.13  | 163.72  | 161.39  | 161.01  | 156.9  | 159.75 | 2.87 |
| bisheng    | 156.79  | 157.14  | 159.55  | 153.87  | 160.12  | 152.38 | 156.64 | 3.05 |

```python
import numpy as np
import pandas as pd
import scipy.stats as stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_rel
from scipy.stats import shapiro, levene

# data
scores = {
    'openjdk': [158.67, 155.67, 157.48, 164.16, 158.79, 159.2],
    'dragonwell': [157.55, 160.77, 159.32, 164.34, 157.42, 160.06],
    'kona': [159.39, 156.13, 163.72, 161.39, 161.01, 156.9],
    'bisheng': [156.79, 157.14, 159.55, 153.87, 160.12, 152.38]
}

# x轴
x = list(range(1, len(scores['openjdk']) + 1))

# 创建图表
plt.figure(figsize=(10, 6))

# 绘制每个 JVM 的曲线
for jvm, score in scores.items():
    plt.plot(x, score, marker='o', label=jvm)

# 添加图表信息
plt.title('SPECjvm2008 Scores Over Time')
plt.xlabel('Test Number')
plt.ylabel('SPECjvm2008 Score')
plt.legend()
plt.grid(True)

# 显示图表
plt.tight_layout()
plt.show()


# 计算均值和标准偏差
means = {key: np.mean(value) for key, value in scores.items()}
std_devs = {key: np.std(value, ddof=1) for key, value in scores.items()}


# 可视化
labels = list(scores.keys())
mean_values = list(means.values())
std_dev_values = list(std_devs.values())

print(mean_values)
print(std_dev_values)

x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots()
bars = ax.bar(x, mean_values, width, yerr=std_dev_values, capsize=5, color=['blue', 'orange', 'green', 'red'])

# 添加文本标签
ax.set_ylabel('Average SPECjvm2008 Score')
ax.set_title('Average SPECjvm2008 Scores by JVM')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.yaxis.grid(True)

# 显示均值值
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2.0, yval, round(yval, 2), va='bottom')

plt.tight_layout()
plt.show()

# 细致可视化均值和方差
plt.figure(figsize=(10, 6))
for jvm in scores:
    plt.errorbar(jvm, means[jvm], yerr=std_devs[jvm], fmt='o', capsize=5, label=jvm)
plt.ylabel('SPECjvm2008 Score')
plt.title('Average SPECjvm2008 Scores with Standard Deviation')
plt.legend()
plt.grid(True)
plt.show()
```

![jvm_折线图](D:\School\研学\学校\浙江大学\项目\README.assets\jvm_折线图.png)

初步感觉bisheng在测试中得分普遍较低

其余jvm差别不大

![jvm_均值图](D:\School\研学\学校\浙江大学\项目\README.assets\jvm_均值图.png)

更加细致的均值和方差图：

![jvm_方差图](D:\School\研学\学校\浙江大学\项目\README.assets\jvm_方差图.png)

## 显著性检验

### 参考博客

[[关于显著性检验，你想要的都在这儿了！！（基础篇）](https://www.cnblogs.com/hdu-zsk/p/6293721.html)](https://www.cnblogs.com/hdu-zsk/p/6293721.html)

> 显著性检验可以分为参数检验和非参数检验。
>
> * 参数检验要求样本来源于正态总体（服从正态分布），且这些正态总体拥有相同的方差，在这样的基本假定（正态性假定和方差齐性假定）下检验各总体均值是否相等，属于参数检验。
>
> * 当数据不满足正态性和方差齐性假定时，参数检验可能会给出错误的答案，此时应采用基于秩的非参数检验。

### 参数检验

> **正态性检验**用于测试数据是否来自正态分布。
>
> 常用的正态性检验方法包括 Shapiro-Wilk 检验 ,特别适合样本量较小（一般在 3 到 5000 之间）的数据集。
>
> **统计量 (W)**：越接近 1 表示数据越符合正态分布。
>
> **p 值**：较小的 p 值（通常 < 0.05）表示拒绝数据符合正态分布的原假设。

> **方差齐性检验**用于测试多个样本的方差是否相等。常用的方法包括 Levene 检验 ,Levene 检验适合用于各种分布的数据，包括正态分布和非正态分布的数据。当数据包含离群值或不是严格正态分布时，Levene 检验是优选方法。
>
> **统计量 (W)**：衡量组间的方差差异。
>
> **p 值**：较小的 p 值（通常 < 0.05）表示拒绝方差齐性的原假设，说明组间方差存在显著差异。

```
openjdk Shapiro-Wilk Test: p-value = 0.2734
dragonwell Shapiro-Wilk Test: p-value = 0.3937
kona Shapiro-Wilk Test: p-value = 0.7710
bisheng Shapiro-Wilk Test: p-value = 0.6104

Levene Test for Homogeneity of Variances: p-value = 0.9116
```

全部的jdk scores都通过了正态性检验和方差齐性检验，可以使用参数检验的方法

### 配对t检验

```python
# JVM 名称列表
jvms = list(scores.keys())
n = len(jvms)

# 初始化 p 值矩阵
p_values_matrix = np.zeros((n, n))

# 计算 p 值矩阵
for i in range(n):
    for j in range(n):
        if i != j:
            _, p_value = ttest_rel(scores[jvms[i]], scores[jvms[j]])
            p_values_matrix[i, j] = p_value
        else:
            p_values_matrix[i, j] = np.nan  # 对角线置为 NaN

# 创建热力图
plt.figure(figsize=(10, 8))
sns.heatmap(p_values_matrix, annot=True, cmap="RdYlBu_r", xticklabels=jvms, yticklabels=jvms, 
            cbar_kws={'label': 'p-value'}, linewidths=0.5, linecolor='gray')

# 设置标题和标签
plt.title('Paired t-test p-value Matrix', fontsize=16)
plt.xlabel('JVM', fontsize=14)
plt.ylabel('JVM', fontsize=14)

# 显示图形
plt.show()

```

![jvm_配对t检验图](D:\School\研学\学校\浙江大学\项目\README.assets\jvm_配对t检验图.png)

不同jvm之间的配对t检验p值均>0.05,则说明他们之间性能没用显著性的差异

### 方差检验

```python
# 转换为 DataFrame
df = pd.DataFrame({k: pd.Series(v) for k, v in scores.items()})
df_melt = df.melt(var_name='JVM', value_name='Score')

# 方差分析
model = ols('Score ~ C(JVM)', data=df_melt).fit()
anova_result = sm.stats.anova_lm(model, typ=2)
print(anova_result)
```

 ANOVA（方差分析）结果如下：

|              | sum_sq     | df   | F        | PR(>F)   |
| ------------ | ---------- | ---- | -------- | -------- |
| **C(JVM)**   | 41.046417  | 3    | 1.701882 | 0.198754 |
| **Residual** | 160.788367 | 20   | NaN      | NaN      |

1. **C(JVM)**: 这是研究的因子，代表不同的 JVM 组。
   - **sum_sq（Sum of Squares）**: 41.046417。这是各组间的平方和，反映了不同 JVM 组的得分差异总量。
   - **df（Degrees of Freedom）**: 3。自由度，即 JVM 组的数量减去 1（`k - 1`，其中 `k` 是 JVM 组数）。
   - **F（F-statistic）**: 1.701882。F 统计量，用于衡量各组间的差异是否大于组内的差异。
   - **PR(>F)（p-value）**: 0.198754。p 值，用于判断结果是否显著。通常 p 值小于 0.05 表示显著差异。这里的 p 值为 0.198754，大于 0.05，表示不同 JVM 组之间的得分差异 **不具有统计显著性**。

2. **Residual**: 这是残差，代表组内的变异。
   - **sum_sq（Sum of Squares）**: 160.788367。残差平方和，反映组内数据的变异。
   - **df（Degrees of Freedom）**: 20。残差的自由度，是总样本数减去组数（`N - k`，其中 `N` 是总样本数，`k` 是 JVM 组数）。
   - **NaN**: 这里的 F 和 p 值是 NaN，因为残差本身没有 F 统计量或 p 值。

- **F-statistic（F 值）**: F 值为 1.701882，较小。这表明组间的差异相对于组内的变异不大。
- **p-value（p 值）**: p 值为 0.198754，大于 0.05，说明我们 **无法拒绝原假设**，即认为不同 JVM 组的得分差异 **不显著**。换句话说，不同 JVM 的性能得分可能是相似的，观察到的差异可能是由随机波动引起的。

为保险起见，我再进行了一次方差检验，其有如下优势：

* 单纯使用 t 检验进行两两比较会导致多重比较问题，增加了犯第一类错误（假阳性）的风险。

* 方差检验允许在一次检验中同时比较多个组（多个 JVM），从而保持了整体的显著性水平不变（即减少 Type I 错误的概率）。在比较多个 JVM 时，性能数据可能会有不同的变异性，单独的 t 检验无法揭示总体变异。ANOVA 将组内和组间的变异进行分离，有助于理解变异的来源，检验组间均值的差异是否超过了组内的变异。

## Answer to the Assignment 2

### Why is there run to run performance variation? And What contributes to run-to-run variation?

1. 硬件和软件在长时间高压运行下的导致性能不稳定。

   * CPU等硬件在长时间高压运行下会严重发热，正如在测试过程中我发现我的电脑发热严重，当电脑的 CPU温度过高时，系统会自动降低其运行频率，以减少发热量和防止损坏硬件。这可能会导致运行间的性能差异.

   * 容易受到其他应用程序的影响，且操作系统可能在调度，缓存管理等方面性能会下降。

     虽然在测试过程中我尽量减少了其他应用程序的干扰，但由于我是虚拟机上运行的，难以彻底排除。

2. 程序本身的随机性，导致产生差异

3. **Java 虚拟机 (JVM) 的内部行为**

   * JVM 的垃圾回收行为可能在不同运行中有所不同

   * JIT（Just-In-Time）编译器的行为，包括优化策略、热点代码的编译时间和方法内联等，可能在不同运行中有所差异。

   * 类加载的时间和顺序可能影响测试的初始运行性能。

4. **预热**，我在测试中预热时间统一设置为120s, 不同jdk对预热时间的要求可能不同，这会影响性能。

### How do we validate the factors contributing to run-to-run variation?

1. 为验证硬件和软件在长时间高压运行下的导致性能不稳定是否有显著影响

   同一个版本的jdk，预热时间相同。

   * 实验组：

     我上述已经得到了数据，我在进行测试之前，也进行了长时间的其他测试，电脑已经发热严重。

   * 对照组：

     我让电脑停止运行10分钟后，使用openjdk再次进行总共6次迭代且benmakrs为compress的测试

     ```
     #!/usr/bin/bash
     
     command_control="/usr/lib/jvm/java-8-openjdk-amd64/bin/java -jar SPECjvm2008.jar -ikv -i 6 compress"
     eval $command_control
     cd ./results || exit 1
     mv SPECjvm2008.001/ validate.01/
     cd ..
     ```

   ```
   --- --- --- --- --- --- --- --- ---
   
     Benchmark:   compress
     Run mode:    timed run
     Test type:   multi
     Threads:     4
     Warmup:      120s
     Iterations:  6
     Run length:  240s
   
   Warmup (120s) begins: Sat Jul 06 17:18:27 CST 2024
   Warmup (120s) ends:   Sat Jul 06 17:20:29 CST 2024
   Warmup (120s) result: 172.35 ops/m
   
   Iteration 1 (240s) begins: Sat Jul 06 17:20:29 CST 2024
   Iteration 1 (240s) ends:   Sat Jul 06 17:24:31 CST 2024
   Iteration 1 (240s) result: 171.95 ops/m
   
   Iteration 2 (240s) begins: Sat Jul 06 17:24:31 CST 2024
   Iteration 2 (240s) ends:   Sat Jul 06 17:28:32 CST 2024
   Iteration 2 (240s) result: 170.10 ops/m
   
   Iteration 3 (240s) begins: Sat Jul 06 17:28:32 CST 2024
   Iteration 3 (240s) ends:   Sat Jul 06 17:32:35 CST 2024
   Iteration 3 (240s) result: 172.15 ops/m
   
   Iteration 4 (240s) begins: Sat Jul 06 17:32:35 CST 2024
   Iteration 4 (240s) ends:   Sat Jul 06 17:36:36 CST 2024
   Iteration 4 (240s) result: 171.08 ops/m
   
   Iteration 5 (240s) begins: Sat Jul 06 17:36:36 CST 2024
   Iteration 5 (240s) ends:   Sat Jul 06 17:40:37 CST 2024
   Iteration 5 (240s) result: 171.31 ops/m
   
   Iteration 6 (240s) begins: Sat Jul 06 17:40:37 CST 2024
   Iteration 6 (240s) ends:   Sat Jul 06 17:44:40 CST 2024
   Iteration 6 (240s) result: 171.19 ops/m
   
   Valid run!
   Score on compress: 172.15 ops/m
   ```

    将实验组和对照组的得分进行统计假设检验来确定硬件对性能影响的差异是否具有统计显著性。

   ![jvm_validate01](D:\School\研学\学校\浙江大学\项目\README.assets\jvm_validate01.png)

   ```
    p-value=0.6205599904060364
    Levene test: W-statistic=1.8473890696120698, p-value=0.20394862185678694
    T-test: T-statistic=10.291575509119257, p-value=1.2206799937734425e-06
   ```

   有显著的差异

2. 验证程序本身的随机性有显著影响

   在`~/java_perf/SPECjvm2008/src/spec/benchmarks/compress`下我找到了compress测试程序的源码

   查看源码可知，compress程序是Modified Lempel-Ziv Method (LZW) ，一种无损数据压缩算法

   核心算法使用开放寻址双哈希，相对素数二次探测，模除法第一探测，自适应重置进行块压缩等均是可重复的，并不会带来运行之间的差异。所以我认为对于compress这个测试项目来说，benchmark 本身不存在可以影响得分的随机性，第2点猜想可以排除。

3,4都要找到最佳预热时间才能验证，我花了大量时间尝试去找官方文档查看是否有说明，但是无果

### What are the pros and cons of using arithmetic mean versus geometric mean in summarizing scores?

#### 算术平均值

**定义**：算术平均值是所有得分之和除以得分的数量。

$算术平均值=\frac{1}{n} \sum_{i=1}^{n} x_i$

**优点**：

1. **简单易懂**：计算和理解起来很简单。
2. **直观**：提供了一个直观的中心趋势度量，适合许多日常情况。
3. **适用范围广**：对于分布不偏斜且没有异常值的数据非常有效。

**缺点**：

1. **对异常值敏感**：极高或极低的值会显著影响平均值。
2. **非正态数据**：对于非正态分布的数据或范围较大的数据，可能会产生误导。

#### 几何平均值

**定义**：几何平均值是所有得分相乘后的n次方根。

$\text{几何平均值} = \left( \prod_{i=1}^{n} x_i \right)^{\frac{1}{n}}$

**优点**：

1. **对异常值不敏感**：减少极端值的影响，更鲁棒。
2. **适合比率**：适用于平均增长率、百分比或涉及乘法的任何数据。

**缺点**：

1. **复杂度高**：计算和理解起来较为复杂。
2. **不适用于零/负值**：不能处理零或负值，因为它涉及到乘积和n次方根。
3. **不太直观**：对于不熟悉的人来说，解释可能不够直观。

### Why does SPECjvm2008 use geometric mean? (In fact, it uses hierarchical geometric mean)

1. **性能指标的乘法性质**

   - **一致的比例缩放**：许多性能指标（如执行时间或吞吐量）往往表现为乘法缩放，而不是加法缩放。这意味着性能的相对变化（例如，一个系统快两倍）比绝对变化更为重要。几何平均数能够准确捕捉这种乘法行为。

   - **归一化效果**：当性能被归一化到一个基准时，使用几何平均数可以有效地汇总归一化后的分数，提供一个在不同基准测试下的公平代表。

2. **对极值的敏感度**

   - **降低对异常值的敏感性**：几何平均数降低了数据集中非常高或非常低的值的影响。在性能基准测试中，少数极端分数可能会通过算术平均数对整体平均值产生不成比例的影响。

   - **平衡的汇总**：它平衡了所有基准测试的影响，确保没有单个基准测试对整体分数产生不成比例的影响。

3. **对数特性**

   - **对数一致性**：性能提升通常以比率或百分比表示。几何平均数能够有效汇总比率，使其更适合乘法比较。这对于主要度量是性能比率（如速度提升）的基准测试尤为重要。

   - **对数分布**：性能数据通常遵循对数正态分布，几何平均数是这种分布的最合适的平均值。

4. **分层结构**
   - **汇总子分数**：SPECjvm2008 使用分层几何平均数将子分数汇总到较高层次的类别，然后再汇总成总体分数。这种方法尊重了基准测试的结构，允许在不同层次的汇总中进行有意义的总结。

# Assignment 3

## 安装工具与学习

```
cd ~/java_perf
# perf
sudo apt-get install linux-tools-common linux-tools-$(uname -r)
# FlameGraph
git clone --depth 1 https://github.com/brendangregg/FlameGraph.git
# perf-map-agent
git clone https://github.com/jvm-profiling-tools/perf-map-agent
sudo apt install cmake
cmake .
make
```

> perf-map-agent 是一个 JVM 字节码代理，它可以与 Linux 的 perf 工具协同工作，为 Java 应用程序创建精确的符号信息，以增强性能分析。
>
> 通常，perf 在分析二进制代码时可能缺乏符号信息，导致难以理解热点代码的具体位置。perf-map-agent 则解决了这个问题，使得 perf 能够在分析Java应用时提供代码级别的洞察。

[perf的基本使用方法](https://www.coonote.com/vim-note/perf-usage.html)

[使用 Perf 和火焰图分析 CPU 性能](https://senlinzhan.github.io/2018/03/18/perf/)

[如何读懂火焰图？](https://www.ruanyifeng.com/blog/2017/09/flame-graph.html)

### 使用方法

使用`sudo perf list`命令可以看到 perf 支持的事件，事件有三种类型：Software event、Hardware event 和 Tracepoint event。

* Hardware Event 是由 PMU 硬件产生的事件，比如 cache 命中
* Software Event 是内核软件产生的事件，比如进程切换，tick 数等
* Tracepoint event 是内核中的静态 tracepoint 所触发的事件

`perf stat`用于统计和报告程序执行期间的各种性能计数器（如指令数、CPU 时钟周期、缓存命中率等）

```
perf stat dd if=/dev/zero of=/dev/null count=1000000
```

<hr>
`perf record`，它可以对事件进行采样，将采样的数据收集在一个 **perf.data 的文件中**


下面的命令对系统 CPU 事件做采样，采样时间为 60 秒，每秒采样 99 个事件，`-g`表示记录程序的调用栈。

**`-a`**: 对所有 CPU 进行采样，意味着无论这个进程在那个 CPU 上运行，`perf` 都会捕获到它的事件。

**`-F 99`**: 以 99 Hz 的频率采样，即每秒采样 99 次。这是用来控制采样频率的。

```
sudo perf record -F 99 -ag -- sleep 60
```

- 执行`sudo perf report -n`可以生成报告的预览。
- 执行`sudo perf report -n --stdio`可以生成一个详细的报告。
- 执行`sudo perf script`可以 dump 出 perf.data 的内容。

　　也可以记录某个进程的事件，例如记录进程号为 1641 的进程：

```
sudo perf record -F 99 -p 1641 -ag -- sleep 60
sudo perf script > out.perf   # 将 perf.data 的内容 dump 到 out.perf
```

<hr>


通常的做法是将 out.perf 拷贝到本地机器，在本地生成火焰图：

```
# 折叠调用栈
$ FlameGraph/stackcollapse-perf.pl out.perf > out.folded
# 生成火焰图
$ FlameGraph/flamegraph.pl out.folded > out.svg
```

生成火焰图可以指定参数，–width 可以指定图片宽度，–height 指定每一个调用栈的高度，生成的火焰图，宽度越大就表示CPU耗时越多。

<hr>


```
cd ~/java_perf/perf-map-agent
./bin/create-java-perf-map.sh $PID
```

会生成`/tmp/perf-$PID.map`

更多具体操作在[perf-map-agent官网](https://github.com/jvm-profiling-tools/perf-map-agent)

>A java agent to generate `/tmp/perf-<pid>.map` files for just-in-time(JIT)-compiled methods for use with the [Linux `perf` tools](https://perf.wiki.kernel.org/index.php/Main_Page).

### **Compile for Debugging**

```
# 启用调试信息
-XX:+PreserveFramePointer
-XX:+UnlockDiagnosticVMOptions
-XX:+DebugNonSafepoints
```

* `-XX:+PreserveFramePointer`：保留帧指针，便于 `perf` 工具准确地生成调用堆栈。

* `-XX:+UnlockDiagnosticVMOptions`：解锁 JVM 的诊断选项。

* `-XX:+DebugNonSafepoints`：在非安全点处生成调试信息，以获取更多的调用堆栈信息。

## Starting from my java program

我先写个简单的链表程序

```java
// 定义节点类
class Node {
    public int data;
    public Node next;

    public Node(int data) {
        this.data = data;
        this.next = null;
    }
}

// 定义链表类
class LinkedList {
    private Node head;
    private Node tail;
    private int len;
    // 在链表的末尾添加新节点
    public void append_effective(int data) {
        if (head == null || tail == null) {
            head = new Node(data);
            tail = head;
            len++;
            return;
        }
        Node newTail = new Node(data);
        tail.next = newTail;
        tail = newTail;
        len++;
    }

    public void append_ineffective(int data){
        if (head == null) {
            head = new Node(data);
            head = new Node(data);
            len++;
            return;
        }
        Node current = head;
        while (current.next != null) {
            current = current.next;
        }
        current.next = new Node(data);
        len++;
    }

    public int getlen() {
        return len;
    }

    public Node gethead(){
        return head;
    }
}



// 主类
public class startPerf {
   static void addToList_effective(LinkedList list){
        for (int i = 0; i < 1e5; i++)
            list.append_effective(i);
   }
   static void addToList_ineffective(LinkedList list){
        for (int i = 0; i < 1e5; i++)
           list.append_ineffective(i);
   }
   public static void main(String[] args) {
        LinkedList list01 = new LinkedList();
        LinkedList list02 = new LinkedList();
        addToList_effective(list01);
        addToList_ineffective(list02);
   }
}
```

运行如下命令

```
javac -g startPerf.java

/usr/lib/jvm/java-8-openjdk-amd64/bin/java -XX:+PreserveFramePointer -XX:+UnlockDiagnosticVMOptions -XX:+DebugNonSafepoints startPerf

PID=$(pgrep -f startPerf)

cd ../perf-map-agent
./bin/create-java-perf-map.sh $PID

cd ../perf

sudo perf record -F 120 -p $PID -ag

sudo perf script > out.perf

# 生成火焰图
../../FlameGraph/stackcollapse-perf.pl out.perf > out.folded
../../FlameGraph/flamegraph.pl out.folded > flamegraph.svg

# 打开火焰图（使用默认浏览器）
xdg-open flamegraph.svg
```

![image-20240708110756833](D:\School\研学\学校\浙江大学\项目\README.assets\image-20240708110756833.png)

![image-20240708110829897](D:\School\研学\学校\浙江大学\项目\README.assets\image-20240708110829897.png)

> vim out.perf

![image-20240708111014037](D:\School\研学\学校\浙江大学\项目\README.assets\image-20240708111014037.png)

> sudo perf report

可以看到`addToList_effective`和`append_effective`运行太快，都没有被捕捉到。

除了系统调用和java库外，程序中运行最慢的就是`append_ineffective`

## Perf stat

...em，可能因为我是在虚拟机中运行的，每次我使用Perf stat我整个虚拟机就会卡死...，按ctrl+c完全没用

为此我重启了我的虚拟机十多次，最终我得出了这个结论.

好在perf record是可以使用的

## Perf record

```sh
# 对benmarks为compress进行测试
cd ~/java_perf/SPECjvm2008

/usr/lib/jvm/java-8-openjdk-amd64/bin/java -XX:+PreserveFramePointer -XX:+UnlockDiagnosticVMOptions -XX:+DebugNonSafepoints -jar SPECjvm2008.jar -ikv -i 6 compress 

PID=$(pgrep -f SPECjvm2008.jar)

cd ../perf-map-agent
./bin/create-java-perf-map.sh $PID

cd ../perf

sudo perf record -F 99 -p $PID -ag -- sleep 480

sudo perf script > out.perf

# 生成火焰图
../FlameGraph/stackcollapse-perf.pl out.perf > out.folded
../FlameGraph/flamegraph.pl out.folded > flamegraph.svg

# 打开火焰图（使用默认浏览器）
xdg-open flamegraph.svg
```

> `pgrep` 是一个用于查找正在运行的进程的命令。
>
> `-f` 是 `pgrep` 的一个选项，允许通过完整的命令行进行匹配搜索。

![image-20240707171029965](D:\School\研学\学校\浙江大学\项目\README.assets\image-20240707171029965.png)

用scimark.sparse.large试试

考虑矩阵乘可能存在大量值得优化的地方，所以用上述benmark进行测试

```sh
#!/usr/bin/bash
cd /home/cilinmengye/java_perf/SPECjvm2008

/usr/lib/jvm/java-8-openjdk-amd64/bin/java -XX:+PreserveFramePointer -XX:+UnlockDiagnosticVMOptions -XX:+DebugNonSafepoints -jar SPECjvm2008.jar -ikv -i 2 scimark.sparse.large &

PID=$(pgrep -f SPECjvm2008.jar)

cd ../perf-map-agent
./bin/create-java-perf-map.sh $PID

cd ../perf

sudo perf record -F 99 -p $PID -ag -- sleep 720

sudo perf script > ./second_sparse/out.perf

# 生成火焰图
../FlameGraph/stackcollapse-perf.pl ./second_sparse/out.perf > ./second_sparse/out.folded
../FlameGraph/flamegraph.pl ./second_sparse/out.folded > ./second_sparse/flamegraph.svg

# 打开火焰图（使用默认浏览器）
# xdg-open flamegraph.svg
```

![image-20240707170935000](D:\School\研学\学校\浙江大学\项目\README.assets\image-20240707170935000.png)

## Perf report

* Shared Object：函数所在的二进制文件或库。
* Symbol：函数名称。
* Command: 命令名称

### compress

![image-20240707192913850](D:\School\研学\学校\浙江大学\项目\README.assets\image-20240707192913850.png)

### sparse



![image-20240707191329858](D:\School\研学\学校\浙江大学\项目\README.assets\image-20240707191329858.png)

> Lspec/benchmarks/scimark/sparse/SparseCompRow;::matmult 86.36%
>
> __sched_yield 3.01%

### 导出到SQLite

![image-20240707193336814](D:\School\研学\学校\浙江大学\项目\README.assets\image-20240707193336814.png)

sparse经过perf script > out.perf的原始文本数据

可以从中提取出

命令名 PID 时间戳

​	函数名 （库名）

#### SQLite使用方法

[参考教程](https://www.runoob.com/sqlite/sqlite-installation.html)

[使用SQLite](https://www.liaoxuefeng.com/wiki/1016959663602400/1017801751919456)

```
sudo apt install sqlite3
```

![image-20240707194434164](D:\School\研学\学校\浙江大学\项目\README.assets\image-20240707194434164.png)

```
# 创建数据库
sqlite perf_data.db
# 查看创建的数据库
sqlite>.databases
# 退出
sqlite>.quit
```

上述是在linux中简单使用sqlite，我发现sqlite还可以在python中使用,那我就写个python脚本吧

```python
import sqlite3
import re

conn = sqlite3.connect('perf_data.db')
cursor = conn.cursor()

create_table = """
CREATE TABLE IF NOT EXISTS perfdata (
    command TEXT,
    pid INTEGER,
    timep FLOAT,
    function TEXT,
    lib TEXT
);
"""
cursor.execute(create_table)
conn.commit()

command = ""
pid = ""
timep = 0.0

filepath = "/home/cilinmengye/java_perf/perf/second_sparse/out.perf"

with open(filepath) as file:
    for line in file:
        tokens = line.split()
        tokens = [token.strip('():[]') for token in tokens]
        tklen = len(tokens)
        if tklen >= 5:
            command = ""
            for i in range(tklen - 5 + 1):
                if i != 0:
                    command = command + " "
                command = command + tokens[i]
            pid = tokens[tklen - 5 + 1]
            try:
                timep = float(tokens[tklen - 5 + 2])
            except ValueError:
                print(f"Skipping line due to ValueError: {line} and {tokens[2]}")
                continue
        elif len(tokens) >=3:
            fct = tokens[1].split('+')[0]
            lib = tokens[2]
            insert_table = """
            INSERT INTO perfdata (command, pid, timep,function, lib) VALUES (?, ?, ?, ?, ?);
            """
            record = (command, pid, timep, fct, lib)
            cursor.execute(insert_table, record)
            print(f"{command} {pid} {timep} {fct} {lib}\n")
# 提交更改并关闭连接
conn.commit()
conn.close()
```

![image-20240707211941643](D:\School\研学\学校\浙江大学\项目\README.assets\image-20240707211941643.png)

通过我上述脚本对sparse的out.perf处理，我得到了总共2239608条函数调用

![image-20240707212040278](D:\School\研学\学校\浙江大学\项目\README.assets\image-20240707212040278.png)

通过函数出现次数进行排序，发现Interpreter出现最多，其基本上是由/tmp/perf-536.map这里产生的，难道这是因为我们使用pef检测造成的？

通过火焰图也可以看到，interpreter占用了许多cpu时间！

然后是`unknown`,其基本上是/usr/lib/jvm/java-8-openjdk-amd64/jre/lib/amd64/server/libjvm.so这里产生的

结合火焰图查看也确实如此

## Answer to the Assignment 3

### Discuss the trade off between profiling granularity (frequency of sampling with perf record) and the induced performance overhead. Explain how adjusting sampling frequency can balance diagnostic detail with minimal intrusion on application behavior.

### 1. **高采样频率**

- 优点

  :

  - **更高的细节**: 捕获更多的样本，可以提供更详细的性能洞察，帮助识别微小的性能瓶颈。
  - **高分辨率分析**: 能捕获更多短时间内发生的事件，适合分析短时间内发生的高频问题。

- 缺点

  :

  - **更高的开销**: 增加 CPU 和内存的开销，因为采样本身需要系统资源。
  - **可能影响应用程序行为**: 频繁的采样可能导致被测应用程序的性能下降，从而影响分析结果的准确性。
  - **大量数据**: 生成的数据量更大，需要更多的存储和处理能力。

### 2. **低采样频率**

- 优点

  :

  - **较低的开销**: 对系统资源的消耗较少，适合在生产环境中使用。
  - **最小化应用程序影响**: 采样频率较低，对被测应用程序的干扰最小。
  - **数据量适中**: 生成的数据量适中，便于存储和处理。

- 缺点

  :

  - **细节减少**: 捕获的样本较少，可能会遗漏短时间内发生的高频事件。
  - **分辨率降低**: 细粒度问题可能难以捕获，尤其是当问题是微小而高频时。

### 3. 如何调整采样频率

1. **了解工作负载**

   - **评估应用程序**: 确定应用程序是否为高负载或低负载，以及在哪些情况下需要详细的性能数据。

   - **确定问题类型**: 根据要分析的问题类型决定采样频率。常见性能问题（如 CPU 消耗、高频函数调用）可能需要高采样频率。

2. 测试和调整

   - **进行基准测试**: 先以较低的采样频率运行，并逐渐增加，观察对应用程序性能的影响。

   - **评估数据质量**: 检查捕获的数据是否足够详细来解决当前的分析需求。

   - **调整频率**: 根据数据质量和性能开销，调整采样频率。

