import Chat from "../../app/chat/chat";
import Button from "./Buttom";
import User from "../config";
import Clock from "./clock";

export default function Chat_area() {
  return (
    <section className="flex-1 items-end-safe px-20 py-45 bg-white h-screen overflow-auto">
      <Chat />
      <section className="flex justify-end px-10 py-5">
        <section className="flex gap-2 mr-2">
          <Clock />
          <User />
        </section>
        <Button children={"New Start Chat"} />
      </section>
    </section>
  );
}
