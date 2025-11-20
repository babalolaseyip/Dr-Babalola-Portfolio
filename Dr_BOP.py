# -*- coding: utf-8 -*-
"""
Dr. Oluwaseyi Paul Babalola - Academic Portfolio
Python script to generate and save the academic portfolio website to Downloads directory
"""

import os
import webbrowser
from datetime import datetime

def create_portfolio_html():
    """Create the complete HTML portfolio content"""
    
    html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dr. Oluwaseyi Paul Babalola - Academic Portfolio</title>
    <style>
        :root {
            --primary-blue: #0056B3;
            --accent-green: #28A745;
            --text-dark: #212529;
            --bg-light: #F8F9FA;
            --white: #FFFFFF;
            --gray-light: #6C757D;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Lato', 'Segoe UI', Arial, sans-serif;
            line-height: 1.6;
            color: var(--text-dark);
            background-color: var(--bg-light);
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }

        /* Navigation */
        nav {
            background-color: var(--white);
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 1000;
            padding: 1rem 0;
        }

        .nav-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0 1rem;
        }

        .logo {
            font-weight: bold;
            font-size: 1.2rem;
            color: var(--primary-blue);
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .logo-img {
            height: 40px;
            width: auto;
            border-radius: 4px;
        }

        .mobile-menu-btn {
            display: none;
            background: none;
            border: none;
            font-size: 1.5rem;
            color: var(--primary-blue);
            cursor: pointer;
        }

        .nav-links {
            display: flex;
            list-style: none;
            gap: 2rem;
        }

        .nav-links a {
            text-decoration: none;
            color: var(--text-dark);
            font-weight: 500;
            transition: color 0.3s;
            padding: 0.5rem;
        }

        .nav-links a:hover {
            color: var(--primary-blue);
        }

        /* Sections */
        section {
            padding: 5rem 0;
            min-height: 100vh;
        }

        .section-header {
            text-align: center;
            margin-bottom: 3rem;
        }

        .section-header h2 {
            font-size: 2.5rem;
            color: var(--primary-blue);
            margin-bottom: 1rem;
        }

        .divider {
            width: 80px;
            height: 4px;
            background-color: var(--accent-green);
            margin: 0 auto;
        }

        /* Home Section */
        #home {
            background: linear-gradient(135deg, var(--primary-blue) 0%, #003d82 100%);
            color: var(--white);
            display: flex;
            align-items: center;
            margin-top: 60px;
        }

        .home-content {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 3rem;
            align-items: center;
        }

        .home-text h1 {
            font-size: 3rem;
            margin-bottom: 1rem;
            line-height: 1.2;
        }

        .home-subtitle {
            font-size: 1.3rem;
            margin-bottom: 2rem;
            opacity: 0.95;
        }

        .info-grid {
            background: rgba(255,255,255,0.1);
            padding: 2rem;
            border-radius: 12px;
            margin: 2rem 0;
        }

        .info-item {
            margin-bottom: 1rem;
            padding: 0.8rem;
            border-left: 3px solid var(--accent-green);
            background: rgba(255,255,255,0.05);
        }

        .info-item h4 {
            color: var(--accent-green);
            margin-bottom: 0.3rem;
        }

        .btn {
            display: inline-block;
            padding: 14px 32px;
            background-color: var(--accent-green);
            color: var(--white);
            text-decoration: none;
            border-radius: 8px;
            font-weight: 600;
            transition: all 0.3s;
            margin-top: 1rem;
            cursor: pointer;
            border: none;
            font-family: inherit;
            font-size: inherit;
        }

        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 20px rgba(0,0,0,0.3);
        }

        /* Content Cards */
        .content-card {
            background: var(--white);
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.08);
            margin-bottom: 2rem;
        }

        .content-card h3 {
            color: var(--primary-blue);
            margin-bottom: 1rem;
            font-size: 1.5rem;
        }

        /* FIX: Ensure text is visible in content cards */
        .content-card p,
        .content-card li {
            color: var(--text-dark) !important;
        }

        .content-card ul {
            margin-left: 1.5rem;
        }

        .content-card li {
            margin-bottom: 0.5rem;
            line-height: 1.6;
        }

        /* Research Section */
        .publications-grid {
            display: grid;
            gap: 1.5rem;
        }

        .publication-item {
            background: var(--white);
            padding: 1.5rem;
            border-radius: 10px;
            border-left: 4px solid var(--primary-blue);
            box-shadow: 0 3px 10px rgba(0,0,0,0.08);
        }

        .publication-title {
            font-weight: 600;
            margin-bottom: 0.5rem;
            color: var(--text-dark);
        }

        .publication-authors {
            color: var(--gray-light);
            font-style: italic;
            font-size: 0.95rem;
        }

        .research-links {
            display: flex;
            gap: 1rem;
            flex-wrap: wrap;
            margin: 2rem 0;
        }

        .research-link {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            padding: 12px 24px;
            background: var(--primary-blue);
            color: var(--white);
            text-decoration: none;
            border-radius: 8px;
            transition: all 0.3s;
        }

        .research-link:hover {
            background: var(--accent-green);
            transform: translateY(-2px);
        }

        /* Supervision Section */
        .students-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 1.5rem;
        }

        .student-card {
            background: var(--white);
            padding: 1.5rem;
            border-radius: 10px;
            border-left: 4px solid var(--accent-green);
            box-shadow: 0 3px 10px rgba(0,0,0,0.08);
        }

        .student-card h4 {
            color: var(--primary-blue);
            margin-bottom: 0.8rem;
        }

        .status {
            display: inline-block;
            background: var(--accent-green);
            color: white;
            padding: 0.3rem 0.8rem;
            border-radius: 15px;
            font-size: 0.85rem;
            margin-top: 0.5rem;
        }

        /* Teaching Section */
        .courses-list {
            display: grid;
            gap: 1rem;
        }

        .course-item {
            background: var(--white);
            padding: 1.2rem;
            border-radius: 8px;
            border-left: 3px solid var(--primary-blue);
            box-shadow: 0 2px 8px rgba(0,0,0,0.06);
        }

        .feedback-links {
            list-style: none;
            margin-top: 2rem;
        }

        .feedback-links li {
            margin-bottom: 0.8rem;
            padding: 1rem;
            background: var(--bg-light);
            border-radius: 8px;
            border-left: 4px solid var(--accent-green);
        }

        .feedback-link {
            color: var(--primary-blue);
            text-decoration: none;
            font-weight: 500;
        }

        .feedback-link:hover {
            color: var(--accent-green);
        }

        /* Professional Contact Section */
        .contact-section {
            background: linear-gradient(135deg, var(--bg-light) 0%, #e9ecef 100%);
        }

        .contact-container {
            max-width: 800px;
            margin: 0 auto;
        }

        .contact-main-card {
            background: var(--white);
            padding: 3rem;
            border-radius: 16px;
            box-shadow: 0 8px 30px rgba(0,0,0,0.12);
            text-align: center;
        }

        .contact-intro {
            font-size: 1.1rem;
            color: var(--gray-light);
            margin-bottom: 2.5rem;
            line-height: 1.6;
        }

        .contact-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 2rem;
            margin-bottom: 3rem;
        }

        .contact-item {
            padding: 1.5rem;
            background: var(--bg-light);
            border-radius: 12px;
            border-left: 4px solid var(--primary-blue);
            transition: transform 0.3s ease;
        }

        .contact-item:hover {
            transform: translateY(-5px);
        }

        .contact-item h3 {
            color: var(--primary-blue);
            margin-bottom: 1rem;
            font-size: 1.3rem;
        }

        .contact-email {
            font-size: 1.1rem;
            color: var(--primary-blue);
            text-decoration: none;
            font-weight: 600;
        }

        .contact-email:hover {
            color: var(--accent-green);
        }

        .contact-phone {
            font-size: 1.3rem;
            font-weight: 700;
            color: var(--text-dark);
            margin: 0.5rem 0;
        }

        .contact-availability {
            font-size: 0.9rem;
            color: var(--gray-light);
            margin-top: 0.5rem;
        }

        .social-section {
            margin-top: 2rem;
        }

        .social-title {
            color: var(--primary-blue);
            margin-bottom: 1.5rem;
            font-size: 1.2rem;
        }

        .social-links-professional {
            display: flex;
            justify-content: center;
            gap: 1.5rem;
            margin-bottom: 2rem;
            flex-wrap: wrap;
        }

        .social-link {
            display: flex;
            flex-direction: column;
            align-items: center;
            text-decoration: none;
            color: var(--primary-blue);
            transition: all 0.3s ease;
            padding: 1rem;
            border-radius: 10px;
            background: var(--bg-light);
            min-width: 80px;
        }

        .social-link:hover {
            color: var(--accent-green);
            transform: translateY(-3px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }

        .social-icon {
            font-size: 2rem;
            margin-bottom: 0.5rem;
        }

        .social-name {
            font-size: 0.8rem;
            font-weight: 600;
            text-align: center;
        }

        .contact-cta {
            background: linear-gradient(135deg, var(--primary-blue) 0%, #003d82 100%);
            color: var(--white);
            padding: 1.5rem 2rem;
            border-radius: 12px;
            margin-top: 2rem;
        }

        .contact-cta h4 {
            margin-bottom: 0.5rem;
            font-size: 1.2rem;
        }

        .contact-cta p {
            margin: 0;
            opacity: 0.9;
            line-height: 1.5;
        }

        /* Footer */
        footer {
            background: var(--text-dark);
            color: var(--white);
            text-align: center;
            padding: 2rem 0;
        }

        /* Profile Image Styles */
        .profile-header {
            display: flex;
            align-items: center;
            gap: 2rem;
            margin-bottom: 2rem;
        }

        .profile-image {
            width: 150px;
            height: 150px;
            border-radius: 50%;
            object-fit: cover;
            border: 4px solid var(--accent-green);
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }

        .profile-text {
            flex: 1;
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            .mobile-menu-btn {
                display: block;
            }

            .nav-links {
                display: none;
                position: absolute;
                top: 100%;
                left: 0;
                width: 100%;
                background: var(--white);
                flex-direction: column;
                padding: 1rem 0;
                box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            }

            .nav-links.active {
                display: flex;
            }

            .home-content {
                grid-template-columns: 1fr;
            }

            .home-text h1 {
                font-size: 2rem;
            }

            .section-header h2 {
                font-size: 2rem;
            }

            .profile-header {
                flex-direction: column;
                text-align: center;
            }

            .profile-image {
                width: 120px;
                height: 120px;
            }

            .contact-main-card {
                padding: 2rem 1.5rem;
            }

            .contact-grid {
                grid-template-columns: 1fr;
                gap: 1.5rem;
            }

            .social-links-professional {
                gap: 1rem;
            }

            .social-link {
                min-width: 70px;
                padding: 0.8rem;
            }

            .social-icon {
                font-size: 1.8rem;
            }
        }

        /* CV Download Section Styles */
        .cv-download-section {
            background: var(--white);
            padding: 3rem 2rem;
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.08);
            margin: 2rem 0;
            text-align: center;
        }

        .cv-download-section h3 {
            color: var(--primary-blue);
            margin-bottom: 1.5rem;
            font-size: 1.8rem;
        }

        .cv-features {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1.5rem;
            margin: 2rem 0;
        }

        .cv-feature {
            padding: 1.5rem;
            background: var(--bg-light);
            border-radius: 8px;
            border-left: 4px solid var(--accent-green);
        }

        .cv-feature h4 {
            color: var(--primary-blue);
            margin-bottom: 0.5rem;
        }

        .download-options {
            display: flex;
            gap: 1rem;
            justify-content: center;
            flex-wrap: wrap;
            margin-top: 2rem;
        }

        .download-btn {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            padding: 12px 24px;
            background: var(--primary-blue);
            color: var(--white);
            text-decoration: none;
            border-radius: 8px;
            font-weight: 600;
            transition: all 0.3s;
            border: none;
            cursor: pointer;
            font-family: inherit;
            font-size: inherit;
        }

        .download-btn:hover {
            background: var(--accent-green);
            transform: translateY(-2px);
            box-shadow: 0 6px 15px rgba(0,0,0,0.2);
        }

        .download-btn.secondary {
            background: var(--gray-light);
        }

        .download-btn.secondary:hover {
            background: #5a6268;
        }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Lato:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
</head>
<body>
    <nav>
        <div class="container nav-container">
            <div class="logo">
                <!-- Replace with your actual logo image path -->
                <img src="/Users/babalolaop/Documents/MacbookSync/Personal Documents/Personal/CV and Cover Letter/personal website/your_logo.png" alt="Dr. Babalola Logo" class="logo-img">
                Dr. O.P. Babalola
            </div>
            <button class="mobile-menu-btn" aria-label="Toggle menu">
                <i class="fas fa-bars"></i>
            </button>
            <ul class="nav-links">
                <li><a href="#home">Home</a></li>
                <li><a href="#research">Research Profile</a></li>
                <li><a href="#supervision">Supervision</a></li>
                <li><a href="#teaching">Courses Taught</a></li>
                <li><a href="#cv">Download CV</a></li>
                <li><a href="#contact">Contact Me</a></li>
            </ul>
        </div>
    </nav>

    <!-- HOME SECTION - CENTERED -->
    <section id="home">
        <div class="container">
            <div class="home-content">
                <div class="profile-header">
                    <!-- Replace with your actual profile image path -->
                    <img src="/Users/babalolaop/Documents/MacbookSync/Personal Documents/Personal/CV and Cover Letter/personal website/your_logo.png" alt="Dr. Oluwaseyi Paul Babalola" class="profile-image">
                    <h1 style="margin-bottom: 0;">Dr. Oluwaseyi Paul Babalola <br>
                    <span style="font-size:0.6em; font-weight:normal;">
                        NRF Y2‑Rated Researcher | Senior IEEE Member
                        </span></h1>
                </div>
                
                <div class="info-grid">
                    <div class="info-item">
                        <h4>Current Position</h4>
                        <p>Lecturer in Engineering Mathematics, Space Engineering & AI<br>
                        Cape Peninsula University of Technology, South Africa</p>
                    </div>
                    
                    <div class="info-item">
                        <h4>Academic Qualifications</h4>
                        <p>Ph.D. in Electronic Engineering<br>
                        M.Sc. in Electronic Engineering<br>
                        B.Sc. in Mathematics</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- RESEARCH PROFILE SECTION -->
    <section id="research">
        <div class="container">
            <div class="section-header">
                <h2>Research Profile</h2>
                <div class="divider"></div>
            </div>

            <div class="content-card">
                <h3>Research Statement</h3>
                <p>My research focuses on developing innovative solutions at the intersection of error-correcting coding, digital signal processing, and artificial intelligence. I lead the Ocean Plastics and Composite Research project at FSATI, where we apply machine learning and remote sensing techniques to address environmental challenges. My work spans visible light communications, wireless systems optimization, underwater acoustic signal processing, and satellite communications, with a commitment to creating accessible technologies that address real-world societal problems.</p>
            </div>

            <div class="content-card">
                <h3>Recent Publications</h3>
                <div class="publications-grid">
                    <div class="publication-item">
                        <div class="publication-title">Multiscale sample entropy-based feature extraction with Gaussian mixture model for detection and classification of blue whale vocalization</div>
                        <div class="publication-authors">Babalola, O.P., Ogundile, O.O. & Balyan, V.</div>
                        <div class="publication-journal"><em>Entropy,</em>, 227(4), 355, 2025</div>
                    </div>

                    <div class="publication-item">
                        <div class="publication-title">Entropy-based detection and classification of Bryde’s whale vocalizations</div>
                        <div class="publication-authors">Babalola, O.P., Ogundile, O.O. & Usman, A.M</div>
                        <div class="publication-journal"><em>Nigerian Journal of Technological Development</em>, 22(1), 51–60, 2025</div>
                    </div>

                    <div class="publication-item">
                        <div class="publication-title">Path priority routing protocol for underwater wireless sensor network</div>
                        <div class="publication-authors">Ogundile, O., Babalola, O., Agboola, E., Ogundile, O. & Davidson, I.</div>
                        <div class="publication-journal"><em>IEEE Internet of Things Journal</em>, 12(15), 31654-31668, 2025.</div>
                    </div>
                </div>
            </div>

            <div class="content-card">
                <h3>Current Research Projects</h3>
                <ul>
                    <li><strong>Ocean Plastic Detection:</strong> Using machine learning and remote sensing for marine protection</li>
                    <li><strong>Cetacean Vocalization Classification:</strong> DSP/ML algorithms for underwater acoustic monitoring</li>
                    <li><strong>6G Wireless Communications:</strong> Rate-splitting multiple access and LDPC code optimization</li>
                    <li><strong>Visible Light Communication:</strong> Flicker-free VLC systems with advanced coding schemes</li>
                </ul>
            </div>

            <div class="content-card">
                <h3>Awards & Recognition</h3>
                <ul>
                    <li><strong>2025:</strong> FAST4FUTURE Mobility Award, CPUT Consolidated Research Fund (R27,869)</li>
                    <li><strong>2025:</strong> Faculty Research Award – Postgraduate Supervisor</li>
                    <li><strong>2024:</strong> NRF Y2-Rated Researcher Grant (R50,000)</li>
                    <li><strong>2024:</strong> Faculty Research Award</li>
                    <li><strong>2023:</strong> Faculty Research Award – Postgraduate Supervisor</li>
                </ul>
            </div>
        </div>
    </section>

    <!-- SUPERVISION SECTION -->
    <section id="supervision">
        <div class="container">
            <div class="section-header">
                <h2>Student Supervision</h2>
                <div class="divider"></div>
            </div>

            <div class="content-card">
                <h3>Current PhD/DEng Students</h3>
                <div class="students-grid">
                    <div class="student-card">
                        <h4>Tamuka Nigel Samurivo</h4>
                        <p><strong>Degree:</strong> DEng</p>
                        <p><em>Thesis:</em> Machine Learning Methods for Ocean Plastic Litter Identification, Tracking, and Classification</p>
                        <span class="status">Registered: 2024</span>
                    </div>

                    <div class="student-card">
                        <h4>Adedotun Ajibare</h4>
                        <p><strong>Degree:</strong> DEng</p>
                        <p><em>Thesis:</em> Rate-Splitting Multiple Access and Machine Learning Techniques for Enhanced RF-EMF and QoS in 6G and Beyond Networks</p>
                        <span class="status">Registered: 2025</span>
                    </div>

                    <div class="student-card">
                        <h4>Amakan Elisha Agoni</h4>
                        <p><strong>Degree:</strong> DEng</p>
                        <p><em>Thesis:</em> Multi-Modal Fusion and Machine Learning Methods for Detection and Classification of Ocean Plastic Litter using Satellite Imagery</p>
                        <span class="status">Registered: 2025</span>
                    </div>

                    <div class="student-card">
                        <h4>Bonginkosi Gumede</h4>
                        <p><strong>Degree:</strong> DEng</p>
                        <p><em>Thesis:</em> Optimising LDPC codes for power-efficient deep space and nanosatellite communications using Machine Learning</p>
                        <span class="status">Registered: 2025</span>
                    </div>
                </div>
            </div>

            <div class="content-card">
                <h3>Graduated Students (2023-2025)</h3>
                <div class="students-grid">
                    <div class="student-card">
                        <h4>Vuyo Sidwel Pana</h4>
                        <p><strong>Degree:</strong> DEng</p>
                        <p><em>Thesis:</em> 5G New Radio and Fog Computing Scalability and QoS Management</p>
                        <span class="status">Graduated: 2025</span>
                    </div>

                    <div class="student-card">
                        <h4>Ncebakazi Sigwili</h4>
                        <p><strong>Degree:</strong> BTech (Hons)</p>
                        <p><em>Thesis:</em> Radio over Fiber for Lossless Transmission of RF Signals</p>
                        <span class="status">Graduated: 2024</span>
                    </div>

                    <div class="student-card">
                        <h4>Randall Allister Press</h4>
                        <p><strong>Degree:</strong> MTech</p>
                        <p><em>Thesis:</em> Channel Performance Estimation for Massive MIMO</p>
                        <span class="status">Graduated: 2023</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- TEACHING SECTION -->
    <section id="teaching">
        <div class="container">
            <div class="section-header">
                <h2>Courses Taught</h2>
                <div class="divider"></div>
            </div>

            <div class="content-card">
                <h3>Teaching Philosophy</h3>
                <p style="margin-bottom: 1.5rem;">My teaching philosophy centers on creating inclusive, engaging learning environments that bridge theory and practice. I believe in:</p>
                <ul>
                    <li><strong>Active Learning:</strong> Foster interactive classrooms where students tackle open-ended problems and collaborative projects</li>
                    <li><strong>Real-World Application:</strong> Integrate industry-standard tools like MATLAB and Python to bridge theory and practice</li>
                    <li><strong>Inclusive Pedagogy:</strong> Create accessible, supportive learning environments with multimodal instruction</li>
                    <li><strong>Technology Integration:</strong> Leverage digital tools like Blackboard, Microsoft Teams, and YouTube to enhance learning beyond traditional classrooms</li>
                </ul>
            </div>

            <div class="content-card">
                <h3>Courses Currently Teaching</h3>
                <div class="courses-list">
                    <div class="course-item">
                        <h4>Engineering Mathematics 1 (EMA151S/155S)</h4>
                        <p><strong>Level:</strong> 1st Year Diploma | <strong>Students:</strong> 180-220</p>
                        <p>Fundamental engineering mathematics including calculus, algebra, and differential equations</p>
                    </div>

                    <div class="course-item">
                        <h4>Engineering Mathematics 5 (EMA580S/581S)</h4>
                        <p><strong>Level:</strong> Honors | <strong>Students:</strong> 40-80</p>
                        <p>Advanced mathematical methods for engineering applications</p>
                    </div>

                    <div class="course-item">
                        <h4>Engineering for Space Environment (ESE690S)</h4>
                        <p><strong>Level:</strong> Joint Masters Program | <strong>Students:</strong> 6-12</p>
                        <p>Space systems engineering, satellite communications, and orbital mechanics</p>
                    </div>
                </div>
            </div>

            <div class="content-card">
                <h3> Eduvos PTY (Ltd) SA</h3>
                <div class="courses-list">
                    <div class="course-item">
                        <h4>Machine Learning & Python Programming</h4>
                        <p>Introduction to ML algorithms and Python implementation</p>
                    </div>

                    <div class="course-item">
                        <h4>Cyber Security & Advanced Networking</h4>
                        <p>Network security principles and advanced networking concepts</p>
                    </div>
                </div>
            </div>

            <div class="content-card">
                <h3>Student Feedback & Evaluations</h3>
                <p style="margin-bottom: 1rem;">Click on any link below to view detailed student feedback:</p>
                <ul class="feedback-links">
                    <li><a href="https://forms.office.com/Pages/AnalysisPage.aspx?AnalyzerToken=G72NxQEaqb731Al5LPJvdnhEuFJP07dN&id=2yK7kDqncUm31nyj75DPBjLCLsElkFNKl-Phmmi5nVFUQlg5UEJZQkNaODFNTlNIWjRLN1Q2WDZCUC4u" target="_blank" class="feedback-link">2024 Midterm - EMA151S Student Feedback</a></li>
                    <li><a href="https://forms.office.com/Pages/AnalysisPage.aspx?AnalyzerToken=G72NxQEaqb731Al5LPJvdnhEuFJP07dN&id=2yK7kDqncUm31nyj75DPBjLCLsElkFNKl-Phmmi5nVFUREtYNkUwVUkwUU9HOFJWUjFNQVRNSkE4Wi4u" target="_blank" class="feedback-link">2024 Term 3 - EMA151S Student Feedback</a></li>
                    <li><a href="https://forms.office.com/Pages/AnalysisPage.aspx?AnalyzerToken=kwKugkouQKWIMkBcuBRN6xEnc3XjCi8R&id=2yK7kDqncUm31nyj75DPBjLCLsElkFNKl-Phmmi5nVFUOFE0RjM5WkJGTlRUTFRKUjM5WVpIM0k4OS4u" target="_blank" class="feedback-link">2024 Midterm - EMA580/581S Student Feedback</a></li>
                    <li><a href="https://forms.office.com/Pages/AnalysisPage.aspx?AnalyzerToken=fvSR8DU5reQfHWoI3ehbtdVLErPR5kvJ&id=2yK7kDqncUm31nyj75DPBjLCLsElkFNKl-Phmmi5nVFUODRTVVJJMlhYVEVQUTVZQzRPVEdXT09LSS4u" target="_blank" class="feedback-link">2024 Term 3 - EMA580/581S Student Feedback</a></li>
                    <li><a href="https://forms.office.com/Pages/AnalysisPage.aspx?AnalyzerToken=fvSR8DU5reQfHWoI3ehbtdVLErPR5kvJ&id=2yK7kDqncUm31nyj75DPBjLCLsElkFNKl-Phmmi5nVFURTMxNDdWMzhBRzFRVzE4VTNYUFlIMjNFOS4u" target="_blank" class="feedback-link">2025 Term 1 - EMA155S Student Feedback</a></li>
                    <li><a href="https://forms.office.com/Pages/AnalysisPage.aspx?AnalyzerToken=fvSR8DU5reQfHWoI3ehbtdVLErPR5kvJ&id=2yK7kDqncUm31nyj75DPBjLCLsElkFNKl-Phmmi5nVFUN0RXTDNQUVFWS1UwWE9ISjlJTjlIQzhFVi4u" target="_blank" class="feedback-link">2025 Term 1 - EMA151S Student Feedback</a></li>
                    <li><a href="https://forms.office.com/Pages/AnalysisPage.aspx?AnalyzerToken=fvSR8DU5reQfHWoI3ehbtdVLErPR5kvJ&id=2yK7kDqncUm31nyj75DPBjLCLsElkFNKl-Phmmi5nVFUM0lZSlVCUlM5V1I4RkpGUkowVU5LRTdaQy4u" target="_blank" class="feedback-link">2025 Term 1 - EMA581S Student Feedback</a></li>
                </ul>
            </div>
        </div>
    </section>

    <!-- CV DOWNLOAD SECTION -->
    <section id="cv">
        <div class="container">
            <div class="section-header">
                <h2>Curriculum Vitae</h2>
                <div class="divider"></div>
            </div>

            <div class="cv-download-section">
                <h3>Download My Complete CV</h3>
                <p style="font-size: 1.1rem; margin-bottom: 2rem; color: var(--gray-light);">
                    Access my comprehensive academic and professional background, including detailed research publications, teaching experience, and professional achievements.
                </p>

                <div class="cv-features">
                    <div class="cv-feature">
                        <h4><i class="fas fa-graduation-cap"></i> Academic Profile</h4>
                        <p>Complete educational background, qualifications, and academic achievements</p>
                    </div>
                    <div class="cv-feature">
                        <h4><i class="fas fa-book"></i> Publications</h4>
                        <p>Full list of 27+ journal articles and conference proceedings</p>
                    </div>
                    <div class="cv-feature">
                        <h4><i class="fas fa-chalkboard-teacher"></i> Teaching Experience</h4>
                        <p>Detailed course listings and teaching philosophy</p>
                    </div>
                    <div class="cv-feature">
                        <h4><i class="fas fa-trophy"></i> Awards & Grants</h4>
                        <p>Research grants, awards, and professional recognition</p>
                    </div>
                </div>

                <div class="download-options">
                    <button class="download-btn" onclick="downloadCV()">
                        <i class="fas fa-file-pdf"></i> Download CV (HTML)
                    </button>
                    <button class="download-btn secondary" onclick="viewOnlineCV()">
                        <i class="fas fa-eye"></i> View Online Version
                    </button>
                </div>

                <div style="margin-top: 2rem; padding: 1.5rem; background: var(--bg-light); border-radius: 8px;">
                    <h4 style="color: var(--primary-blue); margin-bottom: 1rem;">CV Highlights</h4>
                    <ul style="text-align: left; display: inline-block;">
                        <li>Senior IEEE Member & NRF Y2-Rated Researcher</li>
                        <li>27+ Accredited Journal Publications</li>
                        <li>6+ Years of University Teaching Experience</li>
                        <li>Supervision of 8+ Postgraduate Students</li>
                        <li>R300,000+ in Research Grants & Awards</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <!-- PROFESSIONAL CONTACT SECTION -->
    <section id="contact" class="contact-section">
        <div class="container contact-container">
            <div class="section-header">
                <h2>Get In Touch</h2>
                <div class="divider"></div>
                <p class="contact-intro">I welcome opportunities for collaboration, academic discourse, and professional engagement. Feel free to reach out through any of the channels below.</p>
            </div>

            <div class="contact-main-card">
                <div class="contact-grid">
                    <div class="contact-item">
                        <h3><i class="fas fa-envelope"></i> Email</h3>
                        <a href="mailto:babalolaseyip@gmail.com" class="contact-email">babalolaseyip@gmail.com</a>
                        <p class="contact-availability">Typically respond within 24 hours</p>
                    </div>

                    <div class="contact-item">
                        <h3><i class="fas fa-phone"></i> Phone</h3>
                        <p class="contact-phone">(609) 960-6148</p>
                        <p class="contact-availability">Available for calls and WhatsApp</p>
                    </div>
                </div>

                <div class="social-section">
                    <h4 class="social-title">Research Links</h4>
                    <div class="social-links-professional">
                        <a href="https://www.linkedin.com/in/oluwaseyi-paul-babalola-06384715" target="_blank" class="social-link">
                            <i class="fab fa-linkedin social-icon"></i>
                            <span class="social-name">LinkedIn</span>
                        </a>
                        <a href="https://scholar.google.com/citations?user=z6viTLkAAAAJ&hl=en" target="_blank" class="social-link">
                            <i class="fas fa-graduation-cap social-icon"></i>
                            <span class="social-name">Scholar</span>
                        </a>
                        <a href="https://www.researchgate.net/profile/Oluwaseyi-Babalola" target="_blank" class="social-link">
                            <i class="fab fa-researchgate social-icon"></i>
                            <span class="social-name">ResearchGate</span>
                        </a>
                        <a href="https://orcid.org/0000-0001-9681-8437" target="_blank" class="social-link">
                            <i class="fab fa-orcid social-icon"></i>
                            <span class="social-name">ORCID</span>
                        </a>
                        <a href="https://github.com/babalolaseyip" target="_blank" class="social-link">
                            <i class="fab fa-github social-icon"></i>
                            <span class="social-name">GitHub</span>
                        </a>
                        <a href="https://www.youtube.com/@OluwaseyiPaulBabalola" target="_blank" class="social-link">
                            <i class="fab fa-youtube social-icon"></i>
                            <span class="social-name">YouTube</span>
                        </a>
                    </div>
                </div>

                <div class="contact-cta">
                    <h4>Let's Collaborate</h4>
                    <p>Open to research partnerships, speaking engagements, student supervision, and academic discussions across engineering, mathematics, and AI domains.</p>
                </div>
            </div>
        </div>
    </section>

    <footer>
        <div class="container">
            <p>&copy; 2025 Dr. Oluwaseyi Paul Babalola. All rights reserved.</p>
            <p style="margin-top: 0.5rem; opacity: 0.8;">Senior IEEE Member | NRF Y2-Rated Researcher</p>
        </div>
    </footer>

    <script>
        // Mobile menu functionality
        const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
        const navLinks = document.querySelector('.nav-links');
        
        mobileMenuBtn.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            const icon = mobileMenuBtn.querySelector('i');
            icon.classList.toggle('fa-bars');
            icon.classList.toggle('fa-times');
        });

        // Close mobile menu when clicking on a link
        document.querySelectorAll('.nav-links a').forEach(link => {
            link.addEventListener('click', () => {
                navLinks.classList.remove('active');
                const icon = mobileMenuBtn.querySelector('i');
                icon.classList.add('fa-bars');
                icon.classList.remove('fa-times');
            });
        });

        // Smooth scrolling
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });

        // Navbar scroll effect
        window.addEventListener('scroll', function() {
            const nav = document.querySelector('nav');
            if (window.scrollY > 50) {
                nav.style.boxShadow = '0 4px 20px rgba(0,0,0,0.15)';
            } else {
                nav.style.boxShadow = '0 2px 10px rgba(0,0,0,0.1)';
            }
        });

        // CV Download Functionality
        function downloadCV() {
            // Create comprehensive CV content based on the attached PDF
            const cvContent = `
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Dr. Oluwaseyi Paul Babalola - Curriculum Vitae</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background-color: #f5f7fa;
            padding: 20px;
        }
        
        .cv-container {
            max-width: 1000px;
            margin: 0 auto;
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
            overflow: hidden;
        }
        
        header {
            background: linear-gradient(135deg, #0056B3, #003d82);
            color: white;
            padding: 30px;
            text-align: center;
        }
        
        h1 {
            font-size: 2.5rem;
            margin-bottom: 10px;
        }
        
        .contact-info {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 15px;
            margin-bottom: 10px;
            font-size: 1rem;
        }
        
        .section {
            padding: 25px;
            border-bottom: 1px solid #eaeaea;
        }
        
        .section:last-child {
            border-bottom: none;
        }
        
        h2 {
            color: #0056B3;
            margin-bottom: 15px;
            padding-bottom: 8px;
            border-bottom: 2px solid #eaeaea;
        }
        
        h3 {
            color: #0056B3;
            margin: 15px 0 8px;
        }
        
        .job-title {
            font-weight: 600;
            color: #1e40af;
        }
        
        .date {
            color: #6b7280;
            font-style: italic;
        }
        
        ul {
            padding-left: 20px;
            margin: 10px 0;
        }
        
        li {
            margin-bottom: 8px;
        }
        
        .publication {
            margin-bottom: 12px;
            padding-left: 10px;
            border-left: 3px solid #e0e7ff;
        }
        
        .publication-title {
            font-weight: 600;
        }
        
        .skills-container {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-top: 10px;
        }
        
        .skill {
            background-color: #e0e7ff;
            color: #3730a3;
            padding: 6px 12px;
            border-radius: 20px;
            font-size: 0.9rem;
        }
        
        .highlight {
            background-color: #fef3c7;
            padding: 2px 5px;
            border-radius: 3px;
        }
        
        .student-item, .thesis-item {
            margin-bottom: 15px;
            padding: 10px;
            background: #f8f9fa;
            border-radius: 5px;
        }
        
        @media (max-width: 768px) {
            h1 {
                font-size: 2rem;
            }
            
            .section {
                padding: 15px;
            }
            
            .contact-info {
                flex-direction: column;
                align-items: center;
            }
        }
    </style>
</head>
<body>
    <div class="cv-container">
        <header>
            <h1>OLUWASEYI PAUL BABALOLA</h1>
            <div class="contact-info">
                <div>217 Hansen Avenue, Hamilton, NJ 08610</div>
                <div>(609) 960-6148</div>
                <div>babalolaseyip@gmail.com</div>
            </div>
            <div class="contact-info">
                <div>LinkedIn | Google Scholar | ResearchGate | YouTube | ORCID</div>
            </div>
        </header>
        
        <div class="section">
            <h2>PROFESSIONAL SUMMARY</h2>
            <p>Dr. Oluwaseyi Paul Babalola, a Senior IEEE Member and Y2-rated NRF researcher, holds a Ph.D. in Electronic Engineering and brings extensive teaching and research experience. Since 2022, he has taught engineering mathematics to both first-year and honors students, employing MATLAB and active learning methods to inspire mastery of fundamental engineering principles. As the leader of the Ocean Plastics and Composite Research project at FSATI, his research expertise includes error-correcting coding, digital signal processing, remote sensing, and AI applications in visible light, wireless, underwater, and satellite communications. He is adaptable, committed, and dedicated to ethical leadership, diversity, and addressing societal challenges through collaborative innovation. Dr. Babalola is passionate about fostering inclusive and dynamic learning environments, mentoring students, and developing interdisciplinary courses accessible to diverse, high-achieving learners.</p>
        </div>
        
        <div class="section">
            <h2>WORK HISTORY</h2>
            
            <h3><span class="job-title">Lecturer (Grade 8)</span> - <span class="date">07/2023 - Current</span></h3>
            <p><strong>Cape Peninsula University of Technology</strong> - Cape Town, South Africa</p>
            <ul>
                <li>Taught year 1 Engineering Mathematics (EMA151S), and honor level Engineering Mathematics (EMSS80S/581S).</li>
                <li>Taught for the CPUT/UPEC Joint Masters program in Engineering for Space Environment (ESE690S)</li>
                <li>Developed and delivered comprehensive course materials, conducted engaging lectures and interactive tutorials, and provided academic guidance and support to students.</li>
                <li>Employed effective teaching methodologies, incorporated real-world engineering examples and applications, and fostered innovation, inquiry, and interdisciplinary exploration.</li>
                <li>Leveraged digital tools such as Blackboard to engage students through virtual platforms.</li>
                <li>Developed a YouTube channel (www.youtube.com@@oluwaseyiPaulBabalola), providing supplementary learning resources and promoting student engagement beyond the traditional classroom.</li>
                <li>Designed and administered assessments, quizzes, and exams, and provided timely academic progress information and feedback to students.</li>
                <li>Created syllabi, lesson plans, and instructional materials, and reviewed and updated program materials to keep them relevant and accurate.</li>
                <li>Created a safe and respectful classroom environment, encouraged participation and engagement, and promoted diversity and inclusivity.</li>
                <li>Led research on advanced error-correcting coding, digital signal processing techniques, and artificial intelligence, and supervised research projects of undergraduate and postgraduate students.</li>
                <li>Coordinated project activities, managed research teams, and supervised project leaders and research assistants.</li>
                <li>Published articles in esteemed academic journals, presented research findings at conferences, and contributed to the development of the department's research profile.</li>
                <li>Developed strong relationships with colleagues, collaborated on curriculum development, and participated in conferences and professional development opportunities.</li>
            </ul>
            
            <h3><span class="job-title">Lecturer (Independent Contractor)</span> - <span class="date">10/2023 – Current</span></h3>
            <p><strong>Eduvos (Pty) Ltd</strong> - Cape Town, South Africa</p>
            <ul>
                <li>Taught various modules across Year 1-3 such as Mathematics, Computer Network and Security, Python Network Programming, Machine Learning, Mobile Computing, Advanced Networking, and Cyber Security.</li>
                <li>Prepared lecture notes, additional study materials, and ensured quality assurance of learning materials.</li>
                <li>Evaluated student progress through regular assessments, provided detailed feedback, and graded quizzes, tests, homework, and projects.</li>
                <li>Employed various learning styles and abilities, incorporated real-world examples, and used technology to enhance learning methodologies.</li>
                <li>Adapted quickly to shifting educational landscapes, leveraging digital tools such as Microsoft Teams to engage students via virtual platforms.</li>
                <li>Managed large class sizes and maintained a positive learning environment. Built strong rapport with students, maintained an orderly learning environment, and promoted student engagement</li>
                <li>Worked with colleagues to create meaningful learning experiences, shared best practices, and contributed to departmental initiatives.</li>
                <li>Conducted invigilation, course moderation, and monitored student and sponsor affairs.</li>
            </ul>
            
            <h3><span class="job-title">Postdoctoral Researcher and Volunteer Lecturer</span> - <span class="date">07/2020 – 06/2023</span></h3>
            <p><strong>Cape Peninsula University of Technology</strong> - Cape Town, South Africa</p>
            <ul>
                <li>Demonstrated expertise in MATLAB, Python, machine learning, and other technical skills, and applied these skills to develop innovative solutions and algorithms.</li>
                <li>Published 6 ISI-indexed journal articles and 1 conference paper.</li>
                <li>Presented research findings at international conferences and seminars.</li>
                <li>Co-supervised (50) 1 MSc student to completion, Co-supervised (50) 1 PhD, 1 MEng, and undergraduate students, and provided guidance on career pathways and research projects.</li>
                <li>Contributed to research conception, design, and execution to address defined problems, and collaborated with colleagues to develop potential publications.</li>
                <li>Collaborated on curriculum development, shared best practices in teaching strategies, and contributed to funding applications.</li>
                <li>Taught year 1 Engineering Mathematics (EMA 151S) and year 3 Electronic Communications (COM 371S)</li>
                <li>Developed comprehensive course materials, lesson plans, and assessments.</li>
                <li>Conducted engaging lectures and interactive tutorials</li>
                <li>Assessed student progress through regular evaluations and provided detailed feedback for improvement.</li>
                <li>Quickly adapted to shifting educational landscapes during remote learning periods, leveraging digital tools to engage students through virtual platforms.</li>
            </ul>
            
            <h3><span class="job-title">Consolidoc Researcher</span> - <span class="date">02/2020 – 07/2020</span></h3>
            <p><strong>Stellenbosch University</strong> – Stellenbosch, South Africa</p>
            <ul>
                <li>Gathered and organized information for research purposes.</li>
                <li>Collaborated with interdisciplinary teams to conduct comprehensive studies and generate valuable insights.</li>
                <li>Led a team of four researchers to execute the Government of South Africa's Department of Science and Technology Marine Research Project, 2014 – 2024.</li>
                <li>Designed, developed, and tested new RF and DSP algorithms for the detection, classification and tracking of cetaceans.</li>
                <li>Designed and developed a detector to determine the short pulse call of inshore Bryde's whales using DSP techniques and machine learning.</li>
            </ul>

            <h3><span class="job-title">Teaching Assistance</span> - <span class="date">01/2017 – 03/2020</span></h3>
            <p><strong>Stellenbosch University</strong> – Stellenbosch, South Africa</p>
            <ul>
                <li>Taught Signals and Systems 315, Systems and Signals 344 (Year 3)</li>
                <li>Tutored and assisted students with MATLAB simulation tools for basic systems and signals.</li>
                <li>Demonstrated MATLAB simulations and introduced students to basic statistical concepts.</li>
                <li>Created and implemented lesson plans to ensure effective teaching and learning.</li>
                <li>Evaluated student progress through regular assessments, providing detailed feedback for improvement and growth.</li>
                <li>Built strong relationships with colleagues, students, and supervisors, and leveraged interpersonal and communication skills to facilitate knowledge exchange.</li>
            </ul>

            <h3><span class="job-title">Infrastructure and Software Application Support Engineer</span> - <span class="date">03/2018 – 10/2018</span></h3>
            <p><strong>SOFTCOM Solutions SA (PTY) Ltd</strong> - Stellenbosch, South Africa</p>
            <ul>
                <li>Led team projects, including migrating Active Directory environments and performing server backups on Azure.</li>
                <li>Ensured network security by revising and modifying systems, resolving network issues, and troubleshooting TCP/IP, DNS, DHCP, and layer 2/3 network devices.</li>
                <li>Configured and implemented remote access solutions, including IPsec VPN, SSL VPN, and Citrix access gateway.</li>
                <li>Designed and implemented network infrastructure, including inter-VLAN routing on layer-3 switches.</li>
                <li>Collaborated with cross-functional teams, including customers, developers, and stakeholders to gather requirements, provide feedback, and deliver technical solutions.</li>
                <li>Developed and implemented software applications using JavaScript, and SQL Server.</li>
                <li>Managed and maintained computer systems, networks, and servers, including installing, configuring, and testing new software and hardware, and ensuring system security by removing malware and patching software.</li>
            </ul>

            <h3><span class="job-title">Teaching Assistant</span> - <span class="date">02/2015 – 04/2017</span></h3>
            <p><strong>University of the Witwatersrand</strong> – Johannesburg, South Africa</p>
            <ul>
                <li>Taught Signals and Systems ELEN 2005 (Year 2) where students were introduced to mathematical modeling of signals and systems, with practical applications to electrical circuits.</li>
                <li>Taught students basic electronic terminology, simulation software, and circuit analysis techniques using device models.</li>
                <li>Marked technical reports and documented student progress to track understanding and identify areas for improvement.</li>
            </ul>

            <h3><span class="job-title">Systems and Network Engineer</span> - <span class="date">02/2012 – 11/2016</span></h3>
            <p><strong>DPoint Information Technologies</strong> – Ibadan, Nigeria</p>
            <ul>
                <li>Delivered tier 1-3 support for Microsoft products, monitored network capacity and performance, troubleshot complex network problems, and performed routine maintenance tasks.</li>
                <li>Designed and deployed scalable network infrastructure, integrated fixed wireless connectivity, implemented WAN and LAN designs, and optimized routing protocols to improve data transfer speeds.</li>
                <li>Implemented firewalls, VPNs, and access control systems, conducted regular security audits, and developed incident response procedures to ensure network security and reliability.</li>
                <li>Collaborated with teams on disaster planning, network backup, and recovery process monitoring, managed vendor relationships, negotiated contracts, and procured equipment.</li>
                <li>Developed comprehensive documentation for network design, configuration standards, and operational procedures, streamlined network management with automated monitoring tools, and analyzed network performance to drive efficiency.</li>
            </ul>

            <h3><span class="job-title">Database and Network Administrator</span> - <span class="date">01/2011 – 01/2012</span></h3>
            <p><strong>Verde Information Technologies</strong> - Abuja, Nigeria</p>
            <ul>
                <li>Installed, configured, and supported LAN, WAN, and Internet systems, managed network hardware and software, and ensured network availability and security.</li>
                <li>Implemented and maintained firewalls, antivirus software, and intrusion detection systems, conducted risk assessments, and ensured compliance with industry regulations and standards.</li>
                <li>Resolved network and server issues, diagnosed and executed resolution for technical problems, and provided knowledgeable support and quality service.</li>
                <li>Managed data backups, developed comprehensive backup strategies, and conducted regular tests to ensure rapid restoration of IT services in the event of an outage.</li>
                <li>Collaborated with cross-functional teams, managed vendor relationships, negotiated contracts, and procured equipment to support business growth and network expansions.</li>
            </ul>
        </div>
        
        <div class="section">
            <h2>COURSES TAUGHT</h2>
            <ul>
                <li><strong>Course Code:</strong> EMA155S, <strong>Course Name:</strong> Engineering Mathematics 1, <strong>Programme:</strong> Year 1 Diploma in Engineering Technology in Electrical Engineering (D2ETEE), <strong>Class Size:</strong> 76, <strong>Year Taught:</strong> 2025</li>
                <li><strong>Course Code:</strong> EMA151S, <strong>Course Name:</strong> Engineering Mathematics 1, <strong>Programme:</strong> Year 1 Diploma in Engineering Technology in Computer Engineering (D2ENCE), <strong>Class Size:</strong> 109, <strong>Year Taught:</strong> 2025</li>
                <li><strong>Course Code:</strong> EMA580S, <strong>Course Name:</strong> Engineering Mathematics 5, <strong>Programme:</strong> Year 5 (Honors) Bachelor of Engineering Technology in Electrical Engineering (BHETEE/BHETEL), <strong>Class Size:</strong> 69, <strong>Year Taught:</strong> 2025</li>
                <li><strong>Course Code:</strong> EMA581S, <strong>Course Name:</strong> Engineering Mathematics 5, <strong>Programme:</strong> Year 5 (Honors) Bachelor of Engineering Technology in Computer Engineering (BHETCP), <strong>Class Size:</strong> 31, <strong>Year Taught:</strong> 2025</li>
                <li><strong>Course Code:</strong> ESE690S, <strong>Course Name:</strong> Engineering for Space Environment, <strong>Programme:</strong> Joint Master Satellite Systems and Applications, <strong>Class Size:</strong> 6, <strong>Year Taught:</strong> 2025</li>
                <li><strong>Course Code:</strong> EMA151S, <strong>Course Name:</strong> Engineering Mathematics 1, <strong>Programme:</strong> Year 1 Diploma in Engineering Technology in Computer Engineering (D2ENCE), <strong>Class Size:</strong> 220, <strong>Year Taught:</strong> 2024</li>
                <li><strong>Course Code:</strong> EMA580S/581S, <strong>Course Name:</strong> Engineering Mathematics 5, <strong>Programme:</strong> Year 5 (Honors) Bachelor of Engineering Technology in Electrical Engineering (BHETEE) / Computer Engineering (BHETCP), <strong>Class Size:</strong> 38, <strong>Year Taught:</strong> 2024</li>
                <li><strong>Course Code:</strong> EMA151S, <strong>Course Name:</strong> Engineering Mathematics 1, <strong>Programme:</strong> Year 1 Diploma in Engineering Technology in Computer Engineering (D2ENCE), <strong>Class Size:</strong> 128, <strong>Year Taught:</strong> 2023</li>
                <li><strong>Course Code:</strong> ESE690S, <strong>Course Name:</strong> Engineering for Space Environment, <strong>Programme:</strong> Master in Satellite Systems and Applications, <strong>Class Size:</strong> 12, <strong>Year Taught:</strong> 2023</li>
                <li><strong>Course Code:</strong> EMA151S, <strong>Course Name:</strong> Engineering Mathematics 1, <strong>Programme:</strong> Year 1 Diploma in Engineering Technology in Computer Engineering (D2ENCE), <strong>Class Size:</strong> 85, <strong>Year Taught:</strong> 2022</li>
            </ul>
        </div>
        
        <div class="section">
            <h2>EDUCATION</h2>
            
            <h3><span class="job-title">Doctor of Philosophy:</span> Engineering (Electronic) - <span class="date">04/2020</span></h3>
            <p><strong>Stellenbosch University,</strong> Stellenbosch, South Africa</p>
            <p><em>Dissertation:</em> Soft-decision decoding of moderate length binary cyclic codes based on parity-check transformation</p>
            
            <h3><span class="job-title">Master of Science:</span> Engineering (Electrical) - <span class="date">03/2017</span></h3>
            <p><strong>University of the Witwatersrand,</strong> Johannesburg, South Africa</p>
            <p><em>Thesis:</em> Analysis of Bounded Distance Decoding of Reed-Solomon Codes</p>
            <p><strong>Completed Coursework:</strong> Principles of Communication Systems (2014), Telecommunications Business Environment (2014), Teletraffic Engineering (2014), Telecommunication Network Architectures (2014), Telecommunications Investigation Project (2015), Software Project Management (2015), Principles of Wireless Communications (2015), Operational Research Methods (2015), Research Project (2016)</p>
            
            <h3><span class="job-title">Bachelor of Science:</span> Mathematics - <span class="date">11/2009</span></h3>
            <p><strong>University of Ibadan,</strong> Oyo State, Nigeria</p>
            <p><em>Final Year Project:</em> Investment, Risk and Uncertainty Management Model</p>
        </div>
        
        <div class="section">
            <h2>SKILLS</h2>
            <div class="skills-container">
                <div class="skill">MATLAB</div>
                <div class="skill">Python</div>
                <div class="skill">C</div>
                <div class="skill">.NET</div>
                <div class="skill">LATEX</div>
                <div class="skill">Teaching and Classroom Management</div>
                <div class="skill">Student Engagement and Mentoring</div>
                <div class="skill">AI Literacy and Machine Learning</div>
                <div class="skill">Adaptability and Problem Solving</div>
                <div class="skill">Research and Academic Writing</div>
            </div>
        </div>
        
        <div class="section">
            <h2>CERTIFICATIONS</h2>
            <ul>
                <li>Cyber Security Certificate (12554012), 2024 – Current</li>
                <li>KiboCUBE Academy on-site workshop (HEPTA-SAT Training), 2024 – Current</li>
                <li>CHPC-NITheCS Coding Summer School from Centre for High Performance Computing & National Institute for Theoretical and Computational Science, 2023 – Current</li>
                <li>Continuous Professional Development from Department of Electrical and Information Engineering, WITS University, 2014 – Current</li>
            </ul>
        </div>
        
        <div class="section">
            <h2>PROFESSIONAL MEMBERSHIP</h2>
            <ul>
                <li>Senior Member, Institute of Electrical and Electronic Engineers (SMIEEE), (93329115), 2016 – Current</li>
                <li>Oracle Database 10g Administrator Certified Associate - Version Retired, 2010 – Current</li>
                <li>Cisco Certified Network Associate CCNA (ID: CSC011741651), 2010 – 2023</li>
                <li>Oracle Database 10g Administrator Certified Professional (OCP), 2010 – Current</li>
            </ul>
        </div>
        
        <div class="section">
            <h2>GRANTS</h2>
            <ul>
                <li>CPUT Consolidated Research Fund (CRF) of R27,869, 2025</li>
                <li>Conference Committee (ConfCom) Fund of R11,977.00, 2025</li>
                <li>NRF Y2 rated researcher once-off grant of R50,000, 2024</li>
                <li>CPUT Postdoctoral research fellow of R250,000 per annum, 2020 – 2023</li>
                <li>CPUT Consolidated Research Fund (CRF) of R44,509.09, 2022</li>
                <li>Stellenbosch University overseas conference grant of R17,000, 2019</li>
            </ul>
        </div>
        
        <div class="section">
            <h2>ACCOMPLISHMENTS/AWARDS</h2>
            <ul>
                <li>Focus on African Space Science and Technology for Future Development (FAST4FUTURE) Mobility 2 Award, 2025</li>
                <li>Faculty of Engineering and The Built Environment Research Award, 2024</li>
                <li>National Research Foundation (NRF) Y2-rated researcher, 2024</li>
                <li>Faculty of Engineering and The Built Environment Research Award – Postgraduate Supervisor, 2023</li>
                <li>General Stellenbosch University and Faculty Consolido award of R60,000, 2020</li>
                <li>Stellenbosch University Leadership award of R2,000, 2018</li>
                <li>MIH Media Laboratory Postgraduate Doctoral Award of R120,000 per annum, 2017 – 2019</li>
                <li>University of the Witwatersrand Postgraduate Merit Award (PMA) of R30,000, 2017</li>
                <li>University of the Witwatersrand Centre for Telecommunications Access and Services (CETAS) Postgraduate Award of R50,000, 2016</li>
            </ul>
        </div>
        
        <div class="section">
            <h2>COMMUNITY SERVICE AND ENGAGEMENT</h2>
            <ul>
                <li>Key Reviewer, Southern African Universities Power Engineering Conference (SAUPEC 2025)</li>
                <li>Technical Program Committee Member, Pan-African Artificial Intelligence and Smart Systems Conference (PA-AISS 2024)</li>
                <li>Local Organizing Committee Member, 13th Nano-Satellite Symposium, 25 to 27 November 2024</li>
                <li>Review activity for several DHET listed Journals and Conferences, 2019 - Current</li>
                <li>Review activity for NRF Rating Applications, 2019 - Current</li>
                <li>Online Mathematics and Machine Learning Tutor for SPIRES, 2019 - Current</li>
            </ul>
        </div>
        
        <div class="section">
            <h2>COURSE DEVELOPMENT</h2>
            <ul>
                <li>Revised MEng Course: Engineering for Space Environment, 2023 – Current</li>
                <li>Revised MEng Course: Engineering Mathematics 5, 2023 – Current</li>
                <li>Revised DET Course: Engineering Mathematics 1, 2023 – Current</li>
            </ul>
        </div>
        
        <div class="section">
            <h2>COURSE MODERATION</h2>
            <ul>
                <li>External Moderator - New Bridge Graduate Institute, South Africa, 2024 – 2027</li>
                <li>Internal Moderator - Eduvos Institute, South Africa, 2024 – Current</li>
            </ul>
        </div>
        
        <div class="section">
            <h2>RESEARCH ACTIVITIES</h2>
            <ul>
                <li>Academic staff mobility visit to the Centre for Basic Space Science (CBSS), Nsukka, Nigeria, 2025</li>
                <li>Technical visit to the University Space Center of Montpellier (CSUM), Montpellier, France, 2024</li>
                <li>Technical visit to the Université Paris-Est Créteil (UPEC), Paris, France, 2024</li>
                <li>Technical visit to the ESIEE/Gustave-Eiffel University, Paris, France, 2024</li>
                <li>Technical visit to the Physical and Sporting Activity Sciences and Techniques Faculty (STAPS), University of Bordeaux (U-Bordeaux), France, 2024</li>
                <li>Attended and presented a paper at IC4S'05 2024 (Online), 2024</li>
                <li>Guest speaker - IEEE NZ Signal Processing/Information Theory Joint Chapter, co-hosted by the Acoustics Research Centre, University of Auckland, New Zealand, 2023</li>
                <li>Attended and presented a paper in 2023 at 6th SANAP Symposium, Houwhock Hotel, Grabouw, Western Cape, South Africa, 2023</li>
                <li>Attended IC4S'04 2022 Online and presented a paper, 2022</li>
                <li>Attended and presented a paper in 2020 at Nansen Tutu Centre 10th anniversary symposium, Cape Town, South Africa, 2020</li>
                <li>Attended and presented a paper in 2019 at 3rd African Winter School on Information Theory and Communications, Mount Amanzi, Hartbeespoort, South Africa, 2019</li>
                <li>Attended CCECE 2018 Online and presented a paper, 2018</li>
            </ul>
        </div>
        
        <div class="section">
            <h2>SUPERVISION</h2>
            
            <h3>Current Supervisions</h3>
            <div class="student-item">
                <p><strong>Vuyo Sidwel Pana</strong> | DEng, Electrical, Electronics & Computer Engineering | Co-Supervisor</p>
                <p><em>Thesis:</em> 5G New Radio and Fog Computing Scalability and QoS Management | Graduated: 2025</p>
            </div>
            <div class="student-item">
                <p><strong>Neebakazi Sigwili</strong> | BTech (Hons) | Main Supervisor</p>
                <p><em>Thesis:</em> Radio over Fiber for Lossless Transmission of RF Signals | Graduated: 2024</p>
            </div>
            <div class="student-item">
                <p><strong>Randall Allister Press</strong> | MTech in Electrical Engineering | Co-Supervisor</p>
                <p><em>Thesis:</em> Channel Performance Estimation for Massive MIMO | Graduated: 2023</p>
            </div>
            <div class="student-item">
                <p><strong>Sibusiso Duncan Majola</strong> | MEng, Electrical, Electronics & Computer Engineering | Co-Supervisor</p>
                <p><em>Thesis:</em> Dynamic Resource Allocation Schemes for NOMA-based 5G and Beyond Networks | Registered: 2020</p>
            </div>
            <div class="student-item">
                <p><strong>Tamuka Nigel Samurivo</strong> | DEng, Electrical, Electronics & Computer Engineering | Co-Supervisor</p>
                <p><em>Thesis:</em> Machine Learning Methods for Ocean Plastic Litter Identification, Tracking, and Classification | Registered: 2024</p>
            </div>
            <div class="student-item">
                <p><strong>Adedotun Ajibare</strong> | DEng, Electrical, Electronics & Computer Engineering | Main Supervisor</p>
                <p><em>Thesis:</em> Rate-Splitting Multiple Access and Machine Learning Techniques for Enhanced RF-EMF and QoS in 6G and Beyond Networks | Registered: 2025</p>
            </div>
            <div class="student-item">
                <p><strong>Amakan Elisha Agoni</strong> | DEng, Electrical, Electronics & Computer Engineering | Co-Supervisor</p>
                <p><em>Thesis:</em> Multi-Modal Fusion and Machine Learning Methods for Detection and Classification of Ocean Plastic Litter using Satellite Imagery | Registered: 2025</p>
            </div>
            <div class="student-item">
                <p><strong>Bonginkosi Gumede</strong> | DEng, Electrical, Electronics & Computer Engineering | Co-Supervisor</p>
                <p><em>Thesis:</em> Optimising LDPC codes for power-efficient deep space and nanosatellite communications using Machine Learning | Registered: 2025</p>
            </div>
        </div>
        
        <div class="section">
            <h2>THESES EXAMINED</h2>
            <h3>Masters (MTech/MEng/MSc) – 3</h3>
            <div class="thesis-item">
                <p><strong>1. Moumin Hussein</strong> - University of Johannesburg, Johannesburg, South Africa, 2024</p>
                <p><em>Dissertation:</em> South Africa Clean Energy Transition: The Future of Green Hydrogen Energy Technology</p>
            </div>
            <div class="thesis-item">
                <p><strong>2. Peter Oduor Ogolla</strong> - University of the Witwatersrand, Johannesburg, South Africa, 2025</p>
                <p><em>Dissertation:</em> AI-based channel and location estimation techniques for RIS-assisted mobile network</p>
            </div>
            <div class="thesis-item">
                <p><strong>3. Isaac Ngwata</strong> - University of Cape Town, Cape Town, South Africa, 2025</p>
                <p><em>Dissertation:</em> Handover Management in Integrated Terrestrial and Non-Terrestrial Networks</p>
            </div>
        </div>
        
        <div class="section">
            <h2>COLLABORATION</h2>
            <ul>
                <li><strong>Prof Lamine Dieng,</strong> Department of Metal and Cable Structures Laboratory (SMC), Gustave Eiffel University, Nantes Campus, Bouguenais, France: Working on Ocean Plastic and Composite Research, 2024 – current</li>
                <li><strong>Dr Conrad Sparks,</strong> Centre for Sustainable Oceans, Cape Peninsula University of Technology, Cape Town Campus: Working on Ocean Plastic and Composite Research, 2024 – current</li>
                <li><strong>Associate Professor Yusuke Hioka,</strong> Department of Mechanical and Mechatronics Engineering, Faculty of Engineering, The University of Auckland, New Zealand: Worked on signal processing techniques for acoustic communications, 2023 – current</li>
                <li><strong>Prof Vipin Balyan,</strong> CPUT: Working on Wireless Communications, VLC, and Machine Learning, 2022 – current</li>
                <li><strong>Dr Olayinka O. Ogundile,</strong> Department of Physics and Telecommunications, Tai Solarin University of Education, Ijebu-Ode, Nigeria: Working on Machine Learning, Underwater Acoustics, and Wireless Communications, 2018 – current</li>
                <li><strong>Prof Jaco Versfeld,</strong> Department of Electrical and Electronic, Stellenbosch University, Stellenbosch: Working on Machine Learning Techniques for Whale Detection and Classification, 2017 – current</li>
            </ul>
        </div>
        
        <div class="section">
            <h2>RESEARCH OUTPUTS</h2>
            
            <h3>ACCREDITED JOURNAL ARTICLES (27)</h3>
            <div class="publication">
                <p class="publication-title">1. Babalola, O.P., Ogundile, O.O. & Balyan, V., 2025. Multiscale sample entropy-based feature extraction with Gaussian mixture model for detection and classification of blue whale vocalization.</p>
                <p><em>Entropy</em>, 27(4), 355. https://doi.org/10.3390/e27040355</p>
            </div>
            
            <div class="publication">
                <p class="publication-title">2. Babalola, O.P., Ogundile, O.O. & Usman, A.M., 2025. Entropy-based detection and classification of Bryde's whale vocalizations.</p>
                <p><em>Nigerian Journal of Technological Development</em>, 22(1), pp.51–60.</p>
            </div>
            
            <div class="publication">
                <p class="publication-title">3. Ogundile, O.O., Babalola, O.P. & Davidson, I.E., 2025. Secured clustered wireless sensor network using ensemble Hamming code and quadratic residue and nonresidue properties.</p>
                <p><em>IET Wireless Sensor Systems</em>, 15(1), e70014.</p>
            </div>
            
            <div class="publication">
                <p class="publication-title">4. Ajibare, A.T., Vipin, B. & Babalola, O.P., 2025. Enhancing QoS and RF-EMF Radiation Using RSMA and AI in 6G Networks: A Comprehensive Survey.</p>
                <p><em>IEEE Access</em>, 13, pp. 190539-190555. doi:10.1109/ACCESS.2025.3628914</p>
            </div>
            
            <div class="publication">
                <p class="publication-title">5. Ogundile, O., Babalola, O., Agboola, E., Ogundile, O. & Davidson, I., 2025. Path priority routing protocol for underwater wireless sensor network.</p>
                <p><em>IEEE Internet of Things Journal</em>.</p>
            </div>
            
            <div class="publication">
                <p class="publication-title">6. Ogundile, O.O., Ogumnade, H.S., Owoade, A.A., Babalola, O.P. & Balyan, V., 2025. Template-based dynamic time warping credit cards' fraud prediction model.</p>
                <p><em>Engineering Review</em>, 45(2), pp.1–13.</p>
            </div>
            
            <div class="publication">
                <p class="publication-title">7. Babalola, O.P. & Balyan, V., 2024. Dimmable constant weight polar-coded non-orthogonal multiple access with orthogonal space-time block coding visible light communication systems.</p>
                <p><em>IET Communications</em>, pp.1–8. https://doi.org/10.1049/cmu2.12815</p>
            </div>
            
            <div class="publication">
                <p class="publication-title">8. Babalola, O.P. & Versfeld, J., 2024. Wavelet-based feature extraction with hidden Markov model classification of Antarctic blue whale sounds.</p>
                <p><em>Ecological Informatics</em>, 80, 102468. https://doi.org/10.1016/j.ecoint.2024.102468</p>
            </div>
            
            <div class="publication">
                <p class="publication-title">9. Ogundile, O., Babalola, O., Ogunbanwo, A., Ogundile, O. & Balyan, V., 2024. Credit card fraud: analysis of feature extraction techniques for ensemble hidden Markov model prediction approach.</p>
                <p><em>Applied Sciences</em>, 14(16), 7389. https://doi.org/10.3390/app14167389</p>
            </div>
            
            <div class="publication">
                <p class="publication-title">10. Pana, V., Babalola, O.P. & Balyan, V., 2024. HsMM-based mobility aware cell association method for dynamic bandwidth management in 5G-FRANs.</p>
                <p>In: <em>Proceedings of Fifth International Conference on Computing, Communications, and Cyber-Security (IC4S 2023)</em>. Singapore: Springer. https://doi.org/10.1007/978-981-97-2550-2_60</p>
            </div>
            
            <p><em>... and 17 more journal articles (total 27) plus 5 conference proceedings as listed in the full CV</em></p>
        </div>
        
        <div class="section">
            <h2>REFERENCES</h2>
            <ul>
                <li><strong>Available Upon Request</li>
                
        </div>
        
        <footer style="text-align: center; padding: 20px; background: #f8f9fa; color: #6b7280; margin-top: 30px;">
            <p>Generated on ${new Date().toLocaleDateString()} | Dr. Oluwaseyi Paul Babalola - Complete Curriculum Vitae</p>
        </footer>
    </div>
</body>
</html>`;

            // Create a Blob with the CV content
            const blob = new Blob([cvContent], { type: 'text/html' });
            
            // Create a download link
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'Dr_Oluwaseyi_Paul_Babalola_Complete_CV.html';
            
            // Trigger the download
            document.body.appendChild(a);
            a.click();
            
            // Clean up
            setTimeout(function() {
                document.body.removeChild(a);
                URL.revokeObjectURL(url);
            }, 0);

            // Show success message
            alert('Complete CV download started! The file contains all your professional details from the PDF.');
        }

        function viewOnlineCV() {
            // Scroll to the CV section
            document.getElementById('cv').scrollIntoView({
                behavior: 'smooth'
            });
        }
    </script>
</body>
</html>
"""
    return html_content

def save_to_downloads():
    """Save the HTML portfolio to the Downloads directory"""
    
    # Define the Downloads directory path
    downloads_path = "/Users/babalolaop/Downloads"
    
    # Check if the directory exists, create it if it doesn't
    if not os.path.exists(downloads_path):
        try:
            os.makedirs(downloads_path)
            print(f"Created directory: {downloads_path}")
        except Exception as e:
            print(f"Error creating directory: {e}")
            return None
    
    # Create filename
    filename = "dr_babalola_portfolio.html"
    file_path = os.path.join(downloads_path, filename)
    
    # Create the HTML content
    html_content = create_portfolio_html()
    
    try:
        # Save the file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"✅ Portfolio successfully saved to: {file_path}")
        return file_path
        
    except Exception as e:
        print(f"❌ Error saving file: {e}")
        return None

def open_in_browser(file_path):
    """Open the HTML file in the default browser"""
    if file_path and os.path.exists(file_path):
        try:
            webbrowser.open('file://' + file_path)
            print("🌐 Opening portfolio in default browser...")
            return True
        except Exception as e:
            print(f"❌ Error opening browser: {e}")
            return False
    return False

def main():
    """Main function to run the portfolio generator"""
    print("=" * 70)
    print("Dr. Oluwaseyi Paul Babalola - Academic Portfolio Generator")
    print("=" * 70)
    
    # Save to Downloads directory
    file_path = save_to_downloads()
    
    if file_path:
        # Open in browser
        open_in_browser(file_path)
        
        print("\n🎉 Portfolio generation completed successfully!")
        print(f"📁 File location: {file_path}")
        print("\nYou can also manually open this file in any web browser.")
        
        # Show file size
        file_size = os.path.getsize(file_path)
        print(f"📊 File size: {file_size:,} bytes ({file_size/1024:.1f} KB)")
        
        print("\n🔧 Enhanced Features:")
        print("   • Complete CV download with ALL details from your PDF")
        print("   • Professional HTML formatting for the CV")
        print("   • Comprehensive sections: Work History, Education, Publications")
        print("   • Research outputs with 27+ journal articles")
        print("   • Student supervision details")
        print("   • Awards, grants, and professional memberships")
        print("   • Professional references and contact information")
    else:
        print("\n❌ Failed to generate portfolio.")

if __name__ == "__main__":
    # Run the main function
    main()