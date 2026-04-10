function sendMessage(){

      


      const input = document.getElementById('input');
      const chat = document.getElementById('chatbox');
      const message = input.value.trim();
      if (!message) return;
    

      chat.innerHTML += '<div class = "user"> You: ' + message + '</div>';
      input.value = '';

      //Send To Flask Backend

      fetch('/chat', {
        method:'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({message:message})
      })

      .then(response => response.json())
      // .then(data => {
      //   // Show bot response
      //   chat.innerHTML += '<div class="bot"> Bot: ' + data.response + '</div>';
      //   chat.scrollTop = chat.scrollHeight;
      // });

      .then(data => {

      // Show typing indicator
      const typing = document.createElement("div");
      typing.className = "bot";
      typing.innerText = "Bot is typing...";
      chat.appendChild(typing);
      chat.scrollTop = chat.scrollHeight;

      setTimeout(() => {
        typing.remove(); // remove typing text

        chat.innerHTML += '<div class="bot"> Bot: ' + data.response + '</div>';
        chat.scrollTop = chat.scrollHeight;

      }, 1500);
    });

    }

    document.getElementById("input").addEventListener("keydown", function(e) {
      if (e.key === "Enter") {
        e.preventDefault();   // prevents newline / form submit
        sendMessage();
      }
      });
