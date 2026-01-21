export default function Button({ children, ...props }) {
   return (
     <button
       {...props}
       className="px-6 py-3 bg-blue-500 text-white rounded hover:bg-blue-600 transition duration-300 cursor-pointer">
       {children}
     </button>
   ); 
}