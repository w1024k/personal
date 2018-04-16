// pages/movie/movie.js
var DETAIL_URL = "https://47.98.212.195/v2/movie/subject/"
Page({
  data: {
    movie:{}
  },

  onLoad: function (options) {
    console.log(options);
    var that = this
    wx.request({
      url: DETAIL_URL+options.id,
      header:{
        'Content-Type': 'json',
      },
      success: function(res){
        that.setData({
          movie:res.data,
        })
      }

    })
  },
})