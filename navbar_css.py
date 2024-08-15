navbar_css = '''
    /* Navbar Styles */
.navbar {
    background: linear-gradient(90deg, #2c3e50, #3498db);
    padding: 0.5rem 1rem;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    transition: all 0.3s ease;
}

.navbar:hover {
    box-shadow: 0 4px 20px rgba(0,0,0,0.15);
}

.navbar-brand {
    font-size: 1.4rem;
    font-weight: bold;
    color: #ffffff;
    text-transform: uppercase;
    letter-spacing: 1px;
    transition: all 0.3s ease;
}

.navbar-brand:hover {
    text-shadow: 0 0 10px rgba(255,255,255,0.5);
}

.navbar-toggler {
    border-color: rgba(255,255,255,0.5);
    transition: all 0.3s ease;
}

.navbar-toggler:hover {
    background-color: rgba(255,255,255,0.1);
}

.navbar-toggler-icon {
    background-image: url("data:image/svg+xml,%3csvg viewBox='0 0 30 30' xmlns='http://www.w3.org/2000/svg'%3e%3cpath stroke='rgba(255, 255, 255, 0.8)' stroke-width='2' stroke-linecap='round' stroke-miterlimit='10' d='M4 7h22M4 15h22M4 23h22'/%3e%3c/svg%3e");
}

.navbar-nav {
    display: flex;
    align-items: center;
}

.navbar-nav .nav-item {
    margin: 0 0.2rem;
}

.navbar-nav .nav-link {
    color: #ffffff;
    font-weight: 500;
    padding: 0.5rem 1rem;
    border-radius: 4px;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}

.navbar-nav .nav-link::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 50%;
    width: 0;
    height: 2px;
    background-color: #ffffff;
    transition: all 0.3s ease;
}

.navbar-nav .nav-link:hover::after,
.navbar-nav .nav-link:focus::after,
.navbar-nav .nav-item.active .nav-link::after {
    width: 100%;
    left: 0;
}

.navbar-nav .nav-link:hover,
.navbar-nav .nav-link:focus {
    color: #f8f9fa;
    background-color: rgba(255,255,255,0.1);
}

.navbar-nav .nav-item.active .nav-link {
    color: #ffffff;
    background-color: rgba(255,255,255,0.2);
}

@media (max-width: 991.98px) {
    .navbar-nav {
        padding-top: 0.5rem;
    }
    .navbar-nav .nav-item {
        margin: 0.2rem 0;
    }
    .navbar-nav .nav-link {
        padding: 0.5rem 1rem;
    }
}

/* Add this for a smooth slide-down animation when toggling on mobile */
@media (max-width: 991.98px) {
    .navbar-collapse {
        max-height: 0;
        overflow: hidden;
        transition: max-height 0.5s ease;
    }
    .navbar-collapse.show {
        max-height: 500px; /* Adjust this value based on your content */
    }
}
    '''