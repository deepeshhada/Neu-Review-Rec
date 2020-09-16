# -*- coding: utf-8 -*-

import numpy as np


class DefaultConfig:

    model = 'MPCN'
    dataset = 'AmazonDigitalMusic'

    # -------------base config-----------------------#
    use_gpu = True
    gpu_id = 0
    multi_gpu = False
    gpu_ids = []

    seed = 2019
    num_epochs = 60
    num_workers = 0

    optimizer = 'Adam'
    weight_decay = 1e-3  # optimizer rameteri
    lr = 2e-3
    loss_method = 'mse'
    drop_out = 0.5

    use_word_embedding = True

    id_emb_size = 32
    query_mlp_size = 128
    fc_dim = 32

    doc_len = 500
    filters_num = 100
    kernel_size = 3

    num_fea = 1  # id feature, review feature, doc feature
    use_review = True
    use_doc = True
    self_att = False

    r_id_merge = 'cat'  # review and ID feature
    ui_merge = 'cat'  # cat/add/dot
    output = 'lfm'  # 'fm', 'lfm', 'other: sum the ui_feature'

    fine_step = False  # save mode in step level, defualt in epoch
    pth_path = ""  # the saved pth path for test
    print_opt = 'default'

    def set_path(self, name):
        '''
        specific
        '''
        self.data_root = f'./dataset/{name}'
        prefix = f'{self.data_root}/train'

        self.user_list_path = f'{prefix}/userReview2Index.npy'
        self.item_list_path = f'{prefix}/itemReview2Index.npy'

        self.user2itemid_path = f'{prefix}/user_item2id.npy'
        self.item2userid_path = f'{prefix}/item_user2id.npy'

        self.user_doc_path = f'{prefix}/userDoc2Index.npy'
        self.item_doc_path = f'{prefix}/itemDoc2Index.npy'

        self.w2v_path = f'{prefix}/w2v.npy'

    def parse(self, kwargs):
        '''
        user can update the default hyperparamter
        '''
        print("load npy from dist...")
        self.users_review_list = np.load(self.user_list_path, encoding='bytes')
        self.items_review_list = np.load(self.item_list_path, encoding='bytes')
        self.user2itemid_list = np.load(self.user2itemid_path, encoding='bytes')
        self.item2userid_list = np.load(self.item2userid_path, encoding='bytes')
        self.user_doc = np.load(self.user_doc_path, encoding='bytes')
        self.item_doc = np.load(self.item_doc_path, encoding='bytes')

        for k, v in kwargs.items():
            if not hasattr(self, k):
                raise Exception('opt has No key: {}'.format(k))
            setattr(self, k, v)

        print('*************************************************')
        print('user config:')
        for k, v in self.__class__.__dict__.items():
            if not k.startswith('__') and k != 'user_list' and k != 'item_list':
                print("{} => {}".format(k, getattr(self, k)))

        print('*************************************************')


class AmazonInstantVideo_Config(DefaultConfig):

    def __init__(self):
        self.set_path('AmazonInstantVideo')

    vocab_size = 49240
    word_dim = 300

    r_max_len = 202

    u_max_r = 13
    i_max_r = 24

    train_data_size = 29700
    test_data_size = 3713
    val_data_size = 3713

    user_num = 5130 + 2
    item_num = 1685 + 2

    batch_size = 128
    print_step = 100


class AmazonLuxuryBeauty_Config(DefaultConfig):

    def __init__(self):
        self.set_path('AmazonLuxuryBeauty')

    vocab_size = 24150
    word_dim = 300

    r_max_len = 202

    u_max_r = 13
    i_max_r = 24

    train_data_size = 27424
    test_data_size = 3421
    val_data_size = 3420

    user_num = 3818 + 2
    item_num = 1581 + 2

    batch_size = 128
    print_step = 100


class AmazonDigitalMusic_Config(DefaultConfig):

    def __init__(self):
        self.set_path('AmazonDigitalMusic')

    vocab_size = 50002
    word_dim = 300

    r_max_len = 202

    u_max_r = 13
    i_max_r = 24

    train_data_size = 51764
    test_data_size = 6471
    val_data_size = 6471

    user_num = 5541 + 2
    item_num = 3568 + 2

    batch_size = 128
    print_step = 100


class AmazonMusicalInstruments_Config(DefaultConfig):

    def __init__(self):
        self.set_path('AmazonMusicalInstruments')

    vocab_size = 50002
    word_dim = 300

    r_max_len = 202

    u_max_r = 13
    i_max_r = 24

    train_data_size = 185121
    test_data_size = 23112
    val_data_size = 23111

    user_num = 27528 + 2
    item_num = 10620 + 2

    batch_size = 128
    print_step = 100
