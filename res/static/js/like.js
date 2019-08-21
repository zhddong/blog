  function fabulous(item_id){
    // console.log("dadafw")
    $.ajax({ 
        url: "index"//layui.setter.base + 'json/user/reg.js' //实际使用请改成服务端真实接口
        ,type:"POST"
        ,data: {id:item_id}
        ,dataType:"json",
        success: function (data) {
          console.log(data.data.state)
          if(data.data.state!=1){
            document.getElementById("color"+item_id).style="color:#FF0000";
      layer.msg('点赞成功', {
            icon: 6
            ,time: 1000
        })
        }
      else {
      layer.msg('已经点过赞了', {
            icon: 6
            ,time: 1000
        })
          }
        }
        });
    }