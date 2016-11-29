var testServiceData = ["Service1", "Service2", "Service3"];
var testNodeData = ["Node1", "Node2", "Node3"];
var testUserData = ["User1", "User2", "User3"];

displayServices = function() {
	var servicesAnchor = document.getElementById('services');
	for (var i = 0; i < testServiceData.length; i++) {
		var serviceElement = document.createElement('label');
		var serviceText = testServiceData[i];
		serviceElement.innerHTML = serviceText;
		servicesAnchor.appendChild(serviceElement);
		var linebreak = document.createElement('br');
		servicesAnchor.appendChild(linebreak);
	}

}

displayNodes = function() {
	var nodeAnchor = document.getElementById('nodes');
	for (var i = 0; i < testNodeData.length; i++) {
		var nodeElement = document.createElement('label');
		var nodeText = testNodeData[i];
		nodeElement.innerHTML = nodeText;
		nodeAnchor.appendChild(nodeElement);
		var linebreak = document.createElement('br');
		nodeAnchor.appendChild(linebreak);
	}
}

displayUsers = function() {
	var userAnchor = document.getElementById('users');
	for (var i = 0; i < testUserData.length; i++) {
		var userElement = document.createElement('label');
		var userText = testUserData[i];
		userElement.innerHTML = userText;
		userAnchor.appendChild(userElement);
		var linebreak = document.createElement('br');
		userAnchor.appendChild(linebreak);
	}
}