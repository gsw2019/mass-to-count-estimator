import logo from '../assets/logo.svg';

function Header(props: { title: string, description: string }) {

  return (
    // className is Tailwind CSS for styling
    <header className="flex items-center justify-between px-6 py-3 border-b">

      {/* Left side: logo + title/description */}
      <div className="flex items-center gap-4">
          <img
              src={logo}
              alt="Logo"
              className="h-50 w-auto"
          />

        <div className="flex flex-col">
          <h1 className="text-xl font-semibold">{props.title}</h1>
          <p className="text-sm text-gray-600">{props.description}</p>
        </div>
      </div>

      {/* Right side: buttons */}
      <div className="flex items-center gap-4">
        <button className="px-4 py-2 text-gray-700 hover:text-black">Login</button>
        <button className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700">Sign Up</button>
      </div>

    </header>
  );

}

export default Header;