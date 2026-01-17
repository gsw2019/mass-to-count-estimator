/*
 * header component for the Mass to Count Estimator application
 * displays the logo, title, description, and login/sign-up buttons.
 */

import logo from '../assets/logo.svg';

function Header() {

  return (
    // className is Tailwind CSS for styling
    <header className="flex items-center justify-between px-0 py-3 border-b-4 border-gray-300 ">

      {/* Left side: logo + title/description */}
      <div className="flex items-center gap-2">
          <img
              src={logo}
              alt="Logo"
              className="h-50 w-auto"
          />

          <div className="flex flex-col self-start">
              <p className="text-6xl font-mono">Mass to Count Estimator</p>
              <p className="text-lg text-gray-400 font-mono">Estimate the number of items based on their total mass.</p>
          </div>
      </div>

      {/* Right side: buttons */}
      <div className="flex flex-col items-center gap-4 pr-15">
          <button className="px-4 py-2 text-white rounded hover:text-cyan-400 w-25 h-12">Login</button>
          <button className="px-4 py-2 text-white rounded hover:text-cyan-400 w-25 h-12">Sign Up</button>
      </div>

    </header>
  );

}

export default Header;