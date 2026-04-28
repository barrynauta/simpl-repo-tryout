<div style="background-color:#f8f8f8;border:1px solid #d1d5da;border-radius:8px;padding:14px 18px;margin-bottom:20px;">
<p>⚠️ <strong>Work in progress — yet to be validated</strong></p>
<hr/>
<p>
📍 <strong>You are here</strong><br/>
<a href="../../../README.md">🏠 Home</a><br/>
    <a href="../../README.md">Cross-Cutting</a><br/>
        <a href="../README.md">Samples</a><br/>
            <strong>Microfrontend Framework</strong><br/>
</p>
</div>

# Microfrontend Framework

Reference implementation of the **Webpack Module Federation** pattern adopted by Simpl-Open frontends — a host *shell* that loads independently-deployed *remote* applications at runtime, allowing each capability team to ship their UI on its own cadence.

The skeleton ships one **shell** plus three **remotes** (Angular, React, Vue) so teams can pick their preferred framework while still federating into the same shell.

Provenance: built by Simpl. Source repository: `iaa/microfrontend-framework`. Owner: IAA team. Licence: EUPL 1.2.

## Components

- [angular-shell/](angular-shell/README.md) — the host shell that loads remote modules.
- [angular-remote/](angular-remote/README.md) — sample Angular remote.
- [react-remote/](react-remote/README.md) — sample React remote.
- [vue-remote/](vue-remote/README.md) — sample Vue remote.

## Source code

- <https://code.europa.eu/simpl/simpl-open/development/iaa/microfrontend-framework>
