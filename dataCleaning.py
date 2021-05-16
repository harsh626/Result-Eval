import pandas as pd

def cleaning(filename):
    df = pd.read_excel(filename)



    # # Applied Mathematics Theory



    AM_1_list = []
    for i in range(0,130):
        AM_1_list.append(df._get_value(i,'AM - 1'))
    AM_1_list


    # # Engineering Physics Theory

    # In[22]:


    EP_1_list = []
    for i in range(0,130):
        EP_1_list.append(df._get_value(i,'EP - 1'))
    EP_1_list


    # # Engineering Chemistry Theory

    # In[18]:


    EC_1_list = []
    for i in range(0,130):
        EC_1_list.append(df._get_value(i,'EC - 1'))
    EC_1_list


    # # Engineering Mechanics

    # In[20]:


    EM_1_list = []
    for i in range(0,130):
        EM_1_list.append(df._get_value(i,'EM'))
    EM_1_list


    # # Basic Electrical Engineering

    # In[21]:


    BEE_1_list = []
    for i in range(0,130):
        BEE_1_list.append(df._get_value(i,'BEE'))
    BEE_1_list


    # # Applied Mathematics Term Work

    # In[23]:


    AM_1_TW_list = []
    for i in range(0,130):
        AM_1_TW_list.append(df._get_value(i,'AM - 1 TW'))
    AM_1_TW_list


    # # Engineering Physics 1 Term Work

    # In[24]:


    EP_1_TW_list = []
    for i in range(0,130):
        EP_1_TW_list.append(df._get_value(i,'EP - 1 TW'))
    EP_1_TW_list


    # # Engineering Chemistry 1 Term Work

    # In[25]:


    EC_1_TW_list = []
    for i in range(0,130):
        EC_1_TW_list.append(df._get_value(i,'EC - 1 TW'))
    EC_1_TW_list


    # # Engineering Mechanics Term Work

    # In[26]:


    EM_TW_list = []
    for i in range(0,130):
        EM_TW_list.append(df._get_value(i,'EM TW'))
    EM_TW_list


    # # Basic Electrical Engineering Term Work

    # In[27]:


    BEE_TW_list = []
    for i in range(0,130):
        BEE_TW_list.append(df._get_value(i,'BEE TW'))
    BEE_TW_list


    # # Workshop

    # In[29]:


    Workshop_list = []
    for i in range(0,130):
        Workshop_list.append(df._get_value(i,'WORKSHOP'))
    Workshop_list


    # # G.P.A

    # In[30]:


    GPA_list = []
    for i in range(0,130):
        GPA_list.append(df._get_value(i,'GPA'))
    GPA_list


    Names_list = []
    for i in range(130):
        Names_list.append(df._get_value(i,'NAME'))

    Result_list = []
    for i in range(130):
        Result_list.append(df._get_value(i,'RESULT'))

    PassFail_list = []
    for i in range(130):
        PassFail_list.append(df._get_value(i,'PASS_FAIL'))

    passs, fail = 0, 0
    for j in PassFail_list:
        if j == 0:
            fail += 1
        else:
            passs += 1  

    pd_df = pd.DataFrame(list(zip(
        Names_list   ,
        AM_1_list ,
        EP_1_list ,
        EC_1_list ,
        EM_1_list ,
        BEE_1_list ,
        Workshop_list ,
        GPA_list        ,
        AM_1_TW_list        ,
        EP_1_TW_list        ,
        EM_TW_list        ,
        BEE_TW_list       ,
        EC_1_TW_list    ,
        Result_list,
        PassFail_list)),
        columns =['Names', 'Applied-Mathematics I' , 'Engineering Physics I' , 
        'Engineering Chemistry I' , 'Engineering Mechanics' , 'Basic Electrical Engineering' ,
         'Workshop','G.P.A','Applied Mathematics Term Work','Engineering Physics Term Work',
         'Engineering Mechanics Term Work','BEE Term Work','Engineering Chemistry Term Work',
         'Result','PassFail'])
    return pd_df