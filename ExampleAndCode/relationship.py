import os
import time
import jieba
import codecs
import chardet
import jieba.posseg as pseg

# content_path= r"E:\onedrive\python_codes\WordCloud\solar\太阳的距离.txt"
# dict_path = r"E:\onedrive\python_codes\WordCloud\solar\soloar_dict.txt"

content_path= r"E:\onedrive\python_codes\WordCloud\红楼梦\红楼梦.txt"
dict_path = r"E:\onedrive\python_codes\WordCloud\红楼梦\Dream_of_the_Red_Chamber_dict.txt"



'''
核心业务代码是 self.gephi_node_name 和 self.gephi_edge  用于处理检查统计的人物
其中 gephi_cofig.gephi_node_name 会统计人物出现的次数，并且生成给 gephi_config.gephi_edege 处理所需要的 _lineNames 

'''





class gephi_config:
    def __init__(self,content_path,dict_path,name_mode = True):
        start = time.time()
        '''
        # 默认path 懒得删了        
        self._content_path = content_path
        self._dict_path = dict_path
        '''
        
        # 获取py文件所在的path
        self._src = os.path.split(os.path.realpath(__file__))[0]
        
        self.local_file_path()
        # 确认生成文件的名称 
        now = self.get_time()
        dirname = os.path.dirname(self._content_path)   
        content_name = os.path.splitext(os.path.split(self._content_path)[1])[0]
        self._dst_node = os.path.join(dirname,(content_name +'gephi_node-' + now +'.csv'))
        self._dst_edge = os.path.join(dirname,(content_name +'gephi_edge-' + now +'.csv'))

        print('生成的节点文件是：{} \n生成的连接文件是：{}'.format(self._dst_node[-19:],self._dst_edge[-19:]))
        
        # 初始化状态、列表、指点对象
        self._name_mode = name_mode # 确定使用那种模式
        self._lineNames= []         # 姓名检索列表
        self._names = {}			# 姓名字典
        self._relationships = {}	# 关系字典
   
        
        
        # 读取self.dict_name内容并且构建出jieba 需要的文本。
        with codecs.open(self._dict_path,'r',self.content_coding(self._dict_path)) as f:
            self._name_list = f.read().split('\r\n')
            list_name = self._name_list
            list_name[-1] = list_name[-1] + ' 10 nr\r\n'
            self._jieba_dict = ' 10 nr\r\n'.join(list_name)
        



        # 进入处理流程
        self.do_first()

        # 打印处理时间
        end = time.time()
        usetime = end - start
        if usetime > 60.0:
            use_min = usetime // 60
            use_sec = int(usetime - (use_min*60))
            print('time cost {}m {}s.'.format(use_min,use_sec))
        else:
            print('time cost {}s.'.format(int(usetime)))
    
    # 本地文件判断
    def local_file_path(self):
        self._local_txt_status = False
        local_txt_path_list = []
        for i in os.listdir(self._src):
            if os.path.splitext(i)[1] != '.txt':
                continue
            
            local_txt_path_list.append(os.path.join(self._src,i))
            self._local_txt_status = True

        # 如果存在 .txt 的文件，通过文件大小判断「小说」与「小说人物」文件
        if self._local_txt_status:
            for txt_path in local_txt_path_list:
                if os.path.getsize(txt_path) > 10000: # 通过文件大小判断那个是主体文件
                    self._content_path = txt_path     # 小说的路径确定
                    print('小说文件是 {}'.format(os.path.split(self._content_path)[1]))
                else:
                    self._dict_path = txt_path        # 小说角色文件路径确定
                    print('人物文件是 {}'.format(os.path.split(self._dict_path)[1]))

            print("get local txt file path.")

    #生成时分秒格式的str
    def get_time(self):
        ISOTIMEFORMAT = r'%H-%M'
        #ISOTIMEFORMAT = r'%y-%m-%d'
        now = time.strftime(ISOTIMEFORMAT, time.localtime())
        return now

    #确认文件编码
    def content_coding(self,path):
        #print(path)
        with open(path,'rb') as f:
            a = chardet.detect(f.read())
            if a['encoding'] == 'gb2312' or a['encoding'] == 'GB2312':
                coding_type = 'gb18030'
            elif a['encoding'] == 'utf-8':
                coding_type = a['encoding']
            elif a['encoding'] == 'UTF-8-SIG':
                coding_type = a['encoding']
            else:
                print("无法确认编码")
            return coding_type
    
    def Synonymous_names(self):
        '''
        对于可能出现类似 贾宝玉、宝玉 两个名字都指同一个人的情况请按照  
        
        贾宝玉
        宝玉

        这样的方式排列到小说角色文件中去
        '''
        
        Synonymous_dict= {}
        n = 0
        len_name_list = len(self._name_list)
        for i in  self._name_list:
            n += 1
            if len(i) > 2 :
                if n == len_name_list:
                    print('- -||')
                    break
                if i[1:] != self._name_list[n]:                    
                    continue
                
                Synonymous_dict[self._name_list[n]] = i
        print('synoymous ：\n{}'.format(Synonymous_dict))
        return Synonymous_dict
        
    # 不精准模式，利用jieba自带的词性判断能自动判断人名，但是经常超出预期。
    def gephi_node(self):
        jieba.load_userdict(self._dict_path) #加载jieba字典
        with codecs.open(self._content_path, "r",self.content_coding(self._content_path)) as f:
            for lines in f.readlines():
                poss = pseg.cut(lines)
                self._lineNames.append([])
                for w in poss:
                    if w.flag != 'nr' or len(w.word) < 2:
                        continue
                    self._lineNames[-1].append(w.word)
                    if self._names.get(w.word) is None:
                        self._names[w.word] = 0
                        self._relationships[w.word] = {}
                    self._names[w.word] += 1
        print('gephi node done!')
        return self._lineNames

    # 使用精准文字模式，只检索指定人名
    def gephi_node_name(self):
        print('start process node')
        Synonymous_dict = self.Synonymous_names()
        name_set = set(self._jieba_dict.split(' 10 nr\r\n'))    # 将jieba所需要文件样式切割成由任务名组成的 name_set
        jieba.load_userdict(self._dict_path)
        with codecs.open(self._content_path, "r",self.content_coding(self._content_path)) as f:
            for lines in f.readlines():							
                poss = jieba.cut(lines)                         # 由于我已经指定了名字，所以没有使用jieba.posseg.cut 方法进行分词,而是使用了 jieba.cut.
                self._lineNames.append([])
                for w in poss:
                    if w not in name_set:                  # 如果关键字不在 name_set 中存在就跳过
                        continue
                    if Synonymous_dict.get(w):             # 如果存在重名，这里是True 判断，所以就算没有重名（synonymous_dict）为空也没事。这里完全是因为红楼梦里面 贾宝玉 宝玉 林黛玉 黛玉 而生
                        w = Synonymous_dict[w]                    
                    self._lineNames[-1].append(w)
                    if self._names.get(w) is None:
                        self._names[w] = 0
                        self._relationships[w] = {}
                    self._names[w] += 1
        print('gephi node done!')
        return self._lineNames

    

    # 获得角色间连接信息
    def gephi_edge(self):	
        print("start to process edge")			
        for line in self._lineNames:			# 对于每一段
            for name1 in line:					
                for name2 in line:				# 每段中的任意两个人
                    if name1 == name2:
                        continue
                    if self._relationships[name1].get(name2) is None:		# 若两人尚未同时出现则新建项
                        self._relationships[name1][name2]= 1
                    else:
                        self._relationships[name1][name2] = self._relationships[name1][name2]+ 1
        print('gephi edge done!')
        return self._relationships

    # 将处理的信息保存为csv文件
    def save_node_and_edge(self):
        with codecs.open(self._dst_node, "a+", "utf-8") as f:
            f.write("Id,Label,Weight\r\n")
            for name, times in self._names.items():
                f.write(name + "," + name + "," + str(times) + "\r\n")

        with codecs.open(self._dst_edge, "a+", "utf-8") as f:
            f.write("Source,Target,Weight\r\n")
            relationships = self.gephi_edge()
            for name, edges in relationships.items():
                for v, w in edges.items():
                    if w > 3:
                        f.write(name + "," + v + "," + str(w) + "\r\n")

    # 处理流程
    def do_first(self):
        if self._name_mode :
            self.gephi_node_name()
        else:
            self.gephi_node()
        self.save_node_and_edge()


if __name__ == '__main__':
    print('开始处理文件，去楼下喝杯茶吧。')
    a = gephi_config(content_path,dict_path,True)     
    print('任务完成，别喝茶了！')  