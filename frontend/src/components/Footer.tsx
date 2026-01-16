/*
 * footer component for the web application
 * displays author's name and links to GitHub and LinkedIn profiles
 */


function Footer() {

  return (
    <div className="footer mt-6 mb-4 text-center text-gray-500 border-t-4 border-gray-300 pt-4">
      <p>Built by Garret Wilson |
        <a href={"https://github.com/gsw2019"} className="pl-2">GitHub</a> |
        <a href={"https://www.linkedin.com/in/garretwilson-cs-mcb/"} className="pl-2">LinkedIn</a>
      </p>
    </div>
  );

}

export default Footer;