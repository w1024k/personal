//index.js
//获取应用实例
const app = getApp()

var top250_url = "https://47.98.212.195/v2/movie/top250"

Page({
  data:{
    title:'加载中...',
    movies:[]
  },

  // bindViewTap: function () {
  //   wx.navigateTo({
  //     url: '../movie/movie'
  //   })
  // },
  
  onLoad:function(){
    var that = this;
    wx.showToast({
      title: '加载中...',
      icon :'loading',
      duration:10000
    });

    wx.request({
      url: top250_url,
      data:{},
      header:{
        'Content-Type':'json',
      },
      success:function(res){
        wx.hideToast();
        var data = res.data;
        console.log(data.subjects);
        that.setData({
          title:data.title,
          movies: data.subjects
        });
      }
    })
  }
})
