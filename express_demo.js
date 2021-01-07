var express = require('express');
var app = express();
var bodyParser = require('body-parser');
 
var fs = require('fs');

var params = {
    "project_name":"孙悟空",
    "project_code":"BB"
}
function changeJson(id,params){
    fs.readFile('./person.json',function(err,data){
        if(err){
            console.error(err);
        }
        var person = data.toString();
        person = JSON.parse(person);
        //把数据读出来,然后进行修改
        for(var i = 0; i < person.data.length;i++){
            if(id == person.data[i].id){
                console.log('id一样的');
                for(var key in params){
                    if(person.data[i][key]){
                        person.data[i][key] = params[key];
                    }
                }
            }
        }
        person.total = person.data.length;
        var str = JSON.stringify(person);
        //console.log(str);
        fs.writeFile('./person.json',str,function(err){
            if(err){
                console.error(err);
            }
            console.log('--------------------修改成功');
            console.log(person.data);
        })
    })
}
// changeJson(1,params);//执行一下

// 创建 application/x-www-form-urlencoded 编码解析
var urlencodedParser = bodyParser.urlencoded({ extended: false })

app.use('/public', express.static('public'));
 
app.get('/index.html', function (req, res) {
   res.sendFile( __dirname + "/" + "index.html" );
})

app.get('/download.html', function (req, res) {
   res.sendFile( __dirname + "/" + "download.html" );
})
app.post('/process_post', urlencodedParser, function (req, res) {
 
	// 输出 JSON 格式
	var response = {
	   "first_name":req.body.first_name,
	   "last_name":req.body.last_name
	};
	console.log(response);
	//修改
	params.project_name = response.first_name;
	params.project_code = response.last_name;
	changeJson(1,params);
	res.sendFile(__dirname+"/"+"public"+"/"+"public.rar");
	// res.sendFile(__dirname+"/"+"public"+"/"+"test.docx");
	// res.end(JSON.stringify('response'));
})

var server = app.listen(8081, function () {
 
  var host = server.address().address
  var port = server.address().port
 
  console.log("应用实例，访问地址为 http://%s:%s", host, port)
 
})