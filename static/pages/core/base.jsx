var React=components.React;
var ReactDOM = components.ReactDOM;

var Base = React.createClass({
	displayName: 'Base',
    componentDidMount: function(){
	    Tools.handleA();
	},
	render: function(){

		return(<div>
			This is the Base page<br/>
			<a href="#/index" data-tohash>click to index page</a>
		</div>)
	}
});

ReactDOM.render(<Base />, document.getElementById("content"));