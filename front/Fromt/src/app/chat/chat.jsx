export default function Chat() {
  return (
    <section className="p-6">
      <textarea
        className="w-full h-34 p-4 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 resize-none"
        placeholder="Type your message here..."
      ></textarea>
    </section>
  );
}
