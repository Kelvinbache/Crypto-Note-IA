import React from "react";

class NameForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = { username: "", password: "" };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({ [event.target.name]: event.target.value });
  }

async handleSubmit(event) {
    event.preventDefault();

    await fetch("http://localhost:8080/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },

      body: JSON.stringify({
        username: this.state.username,
        password: this.state.password,
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log("Success:", data);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  }

  render() {
    return (
      <section className="flex flex-col items-center justify-center h-screen bg-gray-100">
        <div className="bg-white p-8 rounded shadow-md w-96">
          <h2 className="text-2xl font-bold mb-6 text-center">Login</h2>

          <form onSubmit={e => this.handleSubmit(e)}>
            <div className="mb-4">
              <label className="block text-gray-700 mb-2" htmlFor="username">
                Username
              </label>
              <input
                type="text"
                id="username"
                name="username"
                value={this.state.username}
                onChange={this.handleChange}
                className="w-full px-3 py-2 border rounded"
                placeholder="Enter your username"
              />
            </div>
            <div className="mb-6">
              <label className="block text-gray-700 mb-2" htmlFor="password">
                Password
              </label>
              <input
                type="password"
                className="w-full px-3 py-2 border rounded"
                placeholder="Enter your password"
                id="password"
                name="password"
                value={this.state.password}
                onChange={this.handleChange}
              ></input>
            </div>
            <button
              type="submit"
              className="w-full  bg-blue-500 text-white py-2 rounded hover:bg-blue-600 space-x-1 mb-4 cursor-pointer"
            >
              Login
            </button>

            <button className="w-full bg-gray-500 text-white py-2 rounded hover:bg-gray-600">
              <a href="/sing_up">Sign Up</a>
            </button>
          </form>
        </div>
      </section>
    );
  }
}

export default NameForm;
