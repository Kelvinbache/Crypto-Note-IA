import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Login from "./page/login";
import Sing_up from "./page/sing_up.jsx";
import Connection from "./page/Connection.jsx";

export default function App() {
  return (
    <Router>
       <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/sing_up" element={<Sing_up/>} />
        <Route path="/connection" element={<Connection/>} />
       </Routes>
    </Router>
  );
}