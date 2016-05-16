var React=components.React;
var ReactDOM=components.ReactDOM;
var WordCloud = components.echarts.WordCloud;
var BasicColumn = components.echarts.BasicColumn;

 var data1 = [
      {
          name: "Macys",
          value: 6181
      },
      {
          name: "Amy Schumer",
          value: 4386
      }
    ];


//ECharts
var data = [
      {
          name : "测试1",
         data : [90, 113, 140, 30, 70, 60]
      },
        {
            name : "测试2",
            data : [190, 213, 240, 230, 70, 260]
        },
    ];

var xAxisName = ['周一','周二','周三','周四','周五','周六','周日'];



var ThisPage = React.createClass({
    render: function(){
	    return(
			<div>
        	<p>i am index page!!!!!!!!!!!的负担复旦</p>
				<a href="/" data-tohash>click to base page</a>
                <BasicColumn data={data} xAxisName={xAxisName}/>
                <WordCloud data={data1} />
				</div>
		);
	},
});
console.log(document.getElementById("content"));

ReactDOM.render(<ThisPage />, document.getElementById("content"));