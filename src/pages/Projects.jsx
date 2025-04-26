// src/pages/Projects.jsx
import { useState, useEffect } from "react";

const Projects = () => {
  const [projects, setProjects] = useState([]);

  useEffect(() => {
    const fetchProjects = async () => {
      try {
        const response = await fetch("http://localhost:5000/api/projects/");
        const data = await response.json();
        setProjects(data);
      } catch (error) {
        console.error("Error fetching projects:", error);
      }
    };

    fetchProjects();
  }, []);

  return (
    <div className="p-8">
      <h2 className="text-3xl font-bold mb-4">Projects</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {projects.map((project, index) => (
          <div key={index} className="border p-4 rounded shadow">
            <h3 className="text-xl font-semibold">{project.title}</h3>
            <p className="text-sm mt-2">Tech Stack: {project.tech.join(", ")}</p>
            <a href={project.link} target="_blank" rel="noopener noreferrer" className="text-blue-500 underline mt-2 inline-block">
              View Project
            </a>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Projects;
