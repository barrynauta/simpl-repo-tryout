# LLM Council Transcript — Simpl-Open directory structure vs. capability map

**Date:** 2026-04-26 13:06 GMT+2
**Workspace:** `/Users/barrynauta/tmp/repo` (Simpl-Open documentation catalogue)
**Methodology:** Adapted from Karpathy's LLM Council — 5 independent advisors, anonymized peer review, chairman synthesis.

---

## Original question

> please readup on the directory structure based on the capability map and provide advise

## Framed question (sent to all 5 advisors)

A documentation catalogue repository for **Simpl-Open** (an EU open-source data-space middleware) is organised around its capability map. The capability map defines a 4-level hierarchy: **dimension → capability → business service → solution**, across 6 dimensions (Administration, Data, Governance, Infrastructure, Integration, Security). Release 3.0 (Dec 2025) only partially implements the map.

The actual top-level repo layout has **9 directories**: the 6 dimensions **plus**:
- `foundations/` — business processes (BP01–BP13, SA01–SA04), NFRs (NFR01–15), `principles.md`, `architectural-patterns.md`, `glossary.md`, `capability-map.md`, `interoperability.md`, tile media
- `cross-cutting/` — "components that don't map to a single capability"
- `interoperability/` — exists at top level even though `foundations/interoperability.md` was created (the dir was relocated; remnants may exist)
- `_planning/` — internal generation state

Plus root-level files: `README.md` (catalogue index), `capmap.md`, `MAPPING.md`, `references.md`, `definition-of-done.md`, `Functional-and-Technical-Architecture-Specifications.md` (716kB).

**Observed tensions:**
1. The capability map promises `dimension/capability/business-service/solution/` paths, but most dimensions are sparsely populated (Observability lists 8 services; repo has only `dashboarding/monitoring-service`).
2. Business processes & NFRs live under `foundations/` even though they aren't capability-map nodes.
3. `cross-cutting/` is a catch-all — a known anti-pattern.
4. `interoperability` exists in two places (top-level dir + `foundations/interoperability.md`).
5. Solutions inconsistently named (`notification/notification-service` vs. `onboarding/onboarding` duplicating parent name).
6. Major root files (`capmap.md`, F&T spec, MAPPING.md) sit at root rather than under `foundations/`.

**Audience:** Architects, developers, and partners across multiple Simpl-Open vendor teams.

**The decision:** Does the current directory structure faithfully and usefully represent the capability map? Where does it diverge, what should be done about each divergence, and is dimension-first the right organising principle vs. BP-first / role-first / NFR-traceable?

---

## Advisor responses

### The Contrarian

The capability map is a fiction the repo is quietly admitting it can't sustain. Stop pretending otherwise.

**The fatal flaw**: dimension-first taxonomy assumes the map is stable, complete, and the primary navigation key. None of those hold. Release 3.0 is "partial," Observability has 1 of 8 services on disk, and you've already grown three escape hatches (`foundations/`, `cross-cutting/`, root-level files). When 30% of your top-level dirs are exceptions to your organising principle, the principle has lost.

**Cross-cutting is where architectures go to die.** Today it's a catch-all. In 12 months it will be the largest directory and nobody will know what belongs there. Same fate as every `utils/`, `common/`, `misc/` in software history.

**The duplicate `interoperability`** isn't a remnant — it's a tell. Someone tried to fix it, didn't finish, and now readers can't trust either location is canonical. How many other "relocations" are half-done? Audit before adding more.

**The audience question you're dodging**: vendor teams navigate by *the solution they own*. They do not wake up thinking "I work in the Data dimension's Semantics capability." A flat solutions index plus tag-based views (by dimension, by BP, by NFR) would serve them better than forcing a 4-level path that's mostly empty.

**What I'd actually challenge**: are you maintaining this hierarchy because it serves readers, or because the capability map is a governance artefact you're contractually obliged to mirror? Be honest. If it's the latter, the repo structure should optimise for readers and *generate* a capability-map view, not be one.

**Concrete**: kill `cross-cutting/`, resolve interoperability today, and prototype a solution-first layout before sinking more sparse dimension dirs.

### The First Principles Thinker

You're asking the wrong question.

"Does the directory structure faithfully represent the capability map?" assumes the capability map should be the organising principle. Strip that assumption away and ask: **what is this repository for?**

It's a documentation catalogue. Catalogues exist so someone can *find a thing*. Your audience is a vendor engineer who owns or consumes a specific solution. They arrive knowing one of three things: (a) the name of their solution, (b) the business process they're implementing, or (c) the contract/interface they need to integrate against. None of those three entry points is "dimension."

The capability map is a **governance artifact** — it's how the EU programme office reasons about scope, coverage, and gaps. It is not a navigation structure. You have conflated a planning ontology with a filesystem.

Every "tension" you list is a symptom of this conflation:
- `foundations/` exists because BPs and NFRs don't fit the map — *because the map isn't the right spine*.
- `cross-cutting/` is the same admission, more honestly named.
- Sparse dimensions look like failure only because you expected the tree to mirror the map. It mirrors *reality*: what's been built.
- The duplicate `interoperability` is just migration debris, irrelevant to the real question.

**Rebuild from first principles:** flatten to `solutions/<solution-name>/` as the canonical home for every artifact a vendor owns. Keep `capmap.md`, BPs, NFRs, and the F&T spec as **indexes that link into** `solutions/`. The capability map becomes a *view*, not a *directory*. So does BP-first. So does NFR-traceability. One source of truth, many lenses.

You don't have a taxonomy problem. You have a "we made the index the storage" problem.

### The Expansionist

The capability map isn't a constraint, it's a **launchpad**. Stop asking "does the directory faithfully represent capmap?" and start asking "what does this repo become if it works?"

The latent asset nobody's naming: this is the **only navigable index of an EU sovereign data-space middleware in existence**. Vendors, regulators, academics, and downstream dataspaces (Gaia-X, IDSA, EHDS, ENTSO-E energy spaces) will land here. Optimize for that.

Three asymmetric upsides hiding in plain sight:

1. **Make BP-first the headline navigation, keep dimension as a facet.** Business processes (BP01–BP13) are how partners actually consume this — "I'm onboarding a participant," not "I'm browsing Administration." A multi-axis catalogue (BP × dimension × NFR × audience-role) generated from one source of truth turns capmap.md from a directory-shape constraint into a **graph index**. The sparse dimension folders stop looking embarrassing and start looking like a coverage heatmap — instantly valuable telemetry for the program office.

2. **Treat `cross-cutting/` as a feature, not a bug.** Rename it `platform-fabric/` and promote it. Every successful platform (Kubernetes, AWS, SAP BTP) has a fabric layer. The "anti-pattern" framing is wrong here — these are the integration primitives others build on.

3. **The 716kB F&T spec is a goldmine.** Chunk it, cross-link it into every solution README, embed it as the authoritative anchor for AI-assisted partner onboarding. Combined with the capability map as a knowledge graph, you have the substrate for an **MCP server / agent that answers "which Simpl-Open service do I need?"** That's the real product.

Don't refactor toward purity. Refactor toward **discoverability and machine-readability**. Capmap stays canonical; everything else becomes a generated view.

### The Outsider

I just landed in this repo. Here's what confused me in the first sixty seconds.

**The name "foundations" lies.** I'd expect foundational *concepts* — instead I get business processes, NFRs, glossary, AND the capability map itself. If `capability-map.md` is the organising principle of the whole repo, why is it buried three levels of mental indirection deep? Put it at root, or put it in something honestly named like `_spec/` or `reference/`.

**Nine top-level dirs when you advertise six.** A newcomer reads your pitch ("6 dimensions") and then sees `foundations/`, `cross-cutting/`, `interoperability/`, `_planning/` and immediately distrusts the map. Are those dimensions too? Pseudo-dimensions? I have to read prose to find out. That's a failure.

**`cross-cutting/` and `interoperability/` (top-level) and `foundations/interoperability.md`** — pick one. From outside, this looks like three people made three decisions and nobody reconciled. Just delete the duplicate. Today.

**`onboarding/onboarding`** reads like a bug. So does `notification-service` sitting inside `notification/`. As a stranger I cannot tell whether the inner directory is *the* solution or *a* solution among many that haven't shipped yet. If Release 3.0 has one solution per service, collapse the redundant level until there's a second sibling.

**On the bigger question:** dimension-first is fine *as a filing cabinet* but useless as a *landing experience*. I came here to find "the docs for the thing I own." I don't know which dimension my thing lives in. The README needs a flat A–Z solution index and a "I am a [vendor/architect/integrator], start here" router. The taxonomy can stay; the front door has to change.

Stop apologising for sparse dirs in prose. Just don't create the empty branches yet.

### The Executor

Monday morning, here's what you do. You don't refactor the taxonomy. You fix the five things that actively break navigation, and you do them in this order this week.

**Day 1 (2 hours):** Delete top-level `interoperability/`. It's a remnant. `foundations/interoperability.md` wins. One `git mv` of any survivors, one `git rm -rf`, done. Stop debating it.

**Day 2 (3 hours):** Rename `onboarding/onboarding` → `onboarding/onboarding-service` (or whatever the capmap actually says). Grep the repo for inbound links, fix them. Same pass: audit every solution dir for the parent-name duplication smell. Make one rule: solution dir name == solution name from capmap, verbatim.

**Day 3 (1 hour):** Move `capmap.md`, `MAPPING.md`, `definition-of-done.md`, `references.md`, and the F&T spec into `foundations/`. Leave `README.md` at root. Add redirect stubs at old paths for 30 days if partners have bookmarks.

**Day 4:** Add a `STATUS.md` to every dimension dir listing which capmap services are implemented in R3.0 vs. stub vs. not-yet. This is your sparseness problem — it's not a structure problem, it's a discoverability problem. A table fixes it.

**Day 5:** Rename `cross-cutting/` to something concrete based on what's actually in it. If it's three things, make three dirs. "Catch-all" dies by enumeration.

**Don't do:** BP-first or role-first reorg. You'll burn three sprints, break every external link, and partners who already know "my solution lives under my dimension" will revolt. The dimension-first tree is fine. Foundations as a sibling is fine — BPs and NFRs *are* cross-cutting context, not capmap nodes, and pretending otherwise is the bigger lie.

Ship the five fixes. Move on.

---

## Peer review (anonymized)

**Anonymization map (revealed):**
- Response A = The Outsider
- Response B = The First Principles Thinker
- Response C = The Contrarian
- Response D = The Executor
- Response E = The Expansionist

### Reviewer 1

**1. Strongest: B.** B is the only response that names the actual category error: conflating a governance ontology with a filesystem. "You made the index the storage" is the diagnosis the others circle around. Its `solutions/<name>/` proposal with capmap/BP/NFR as generated views dissolves every listed tension instead of patching them. C reaches the same insight but stops at critique; D is tactically excellent but explicitly defends the broken spine; A and E are partial.

**2. Biggest blind spot: D.** D optimises for shipping this week and dismisses structural reorg as sprint-burn — but its own Day 4 (STATUS.md per dimension) is an admission that the dimension tree doesn't carry the information readers need. D is patching a leaky abstraction it refuses to question. The five fixes are right; the "don't reorg" conclusion is wrong because the reorg is what makes the fixes durable.

**3. What ALL missed:** None asked who maintains this and how. A docs catalogue this fragmented across 9 top-level dirs implies multiple writers with no ownership model. Without CODEOWNERS, a contribution guide, or a single editor, any structure — dimension-first, solution-first, BP-first — drifts back to the current state within two releases. Structure follows governance, not the reverse.

### Reviewer 2

**1. Strongest: B.** B reframes correctly: the capmap is a governance ontology, not a navigation structure. Identifying "we made the index the storage" diagnoses the root cause that A, C, and D only circle. Its prescription (`solutions/<name>/` as canonical, every other taxonomy as a generated view) subsumes D's tactical fixes and E's BP-first facet without committing to either as the spine. C reaches the same conclusion less precisely; B names the conflation.

**2. Biggest blind spot: D.** D's "ship five fixes, move on" pragmatism ignores that the duplicate `interoperability` and `cross-cutting` are *symptoms* of the structural conflation B names. Renaming `cross-cutting/` by enumeration treats the rash, not the disease — in another release the catch-all returns under a new name. D also dismisses BP-first reorg on cost grounds without acknowledging that partners genuinely don't navigate by dimension.

**3. What all five missed:** Nobody asked who *writes* into this repo and through what workflow. Structure follows authorship: if dimension owners contribute per-dimension and CI assembles views, dimension-first is correct; if solution teams own folders, B's model wins. Also missed: versioning. R3.0 is "partial" — does R3.1 reshape the tree? A structure that churns each release destroys external links regardless of which taxonomy wins. Governance of the structure matters more than the structure.

### Reviewer 3

**1. Strongest: B.** B reframes the question correctly: the repo conflates a governance ontology (capmap) with a filesystem. "You made the index the storage" is the diagnosis; `solutions/<name>/` with capmap/BP/NFR as generated indexes is the cleanest target state. C reaches the same conclusion less crisply; D is tactically right but ducks the strategic question.

**2. Biggest blind spot: D.** D's "ship five fixes, don't reorg" is seductive but treats symptoms. Every fix (rename `cross-cutting/`, dedupe interoperability, parent-name audit) is paving cowpaths on a spine that B and C correctly identify as wrong. D also asserts partners "already know my solution lives under my dimension" without evidence — the opposite of what A's sixty-second test shows. Tactical excellence applied to a strategic mistake.

**3. What all five missed:** None addressed **versioning and the lifecycle of "Release 3.0 partial."** The repo encodes a moving target: R4.0 will add solutions, rename some, deprecate others. Whatever spine is chosen — dimension, solution, BP — must answer: how does a partner pin to R3.0 docs while R4.0 lands? Where do deprecated solutions live? Is capmap.md itself versioned alongside the tree it shapes? Without a release/lifecycle model, every refactor proposed silently assumes a static snapshot and will re-fragment within one release cycle.

### Reviewer 4

**1. B is strongest.** It correctly diagnoses the root cause: conflating a governance ontology (capmap) with filesystem storage. Its prescription (one source of truth in `solutions/`, everything else as generated views) subsumes D's tactical fixes, C's flat-index instinct, and E's multi-axis dream into a coherent architectural move. A and C circle this insight; B names it.

**2. D has the biggest blind spot.** It treats the symptoms and explicitly forbids the structural conversation ("don't do BP-first or role-first reorg"). Day 1-5 fixes are correct but D mistakes "ship something Monday" for an answer to "is the spine right?" Doing D's week and *also* doing B's redesign are not mutually exclusive — D pretends they are, which protects the wrong status quo. It also dismisses sparseness as a discoverability problem when sparseness is actually evidence the spine doesn't fit reality (C's point).

**3. All five missed: who maintains this, and the link-stability contract.** None ask whether the EU programme office contractually requires the capmap-mirrored tree (governance deliverable vs. reader artifact). None address external bookmarks, vendor PR links, or cross-references from the 716kB F&T spec — any reorg breaks these. None mention how solution-first or BP-first survives Release 4.0/5.0 when capmap itself evolves. The versioning/governance dimension is absent from every response.

### Reviewer 5

**1. Strongest: B.** It diagnoses the root cause — conflating a governance ontology with a filesystem — and prescribes a coherent fix (solutions/ as storage, capmap/BP/NFR as generated views). D is tactically excellent but accepts the flawed spine; B reframes the problem so D's fixes become obvious second-order work. C reaches the same conclusion less rigorously.

**2. Biggest blind spot: E.** It hand-waves migration cost and partner disruption while proposing the most ambitious reframe (BP-first headline, MCP server, knowledge graph). It never engages with: who maintains the generated views, how the F&T spec gets chunked without breaking authoritative status, or the governance reality that the EU programme office likely *requires* capmap-shaped artifacts. Aspirational without a delivery path.

**3. What ALL missed:** None asked who owns the repo's structure decision. Is this contractually constrained by the EU programme office, or is the maintainer free to choose? B hints at it; nobody asks. Also missed: the *write path* — vendors don't just read, they contribute READMEs. A solution-first or view-generated structure changes contribution mechanics (PR templates, CODEOWNERS, review routing). And nobody mentioned versioning: Release 3.0 is "partial" — does R4.0 reshape the tree? A structure that churns per release is worse than any of the alternatives debated.

---

## Chairman synthesis

### Where the council agrees

Five points converged independently across advisors:

1. **Delete the duplicate top-level `interoperability/` today.** The Outsider, First Principles Thinker, Executor, and Expansionist all call it migration debris. Zero defenders. This is free.
2. **Fix `onboarding/onboarding` and similar parent-name duplications.** The Outsider and Executor both flag it; nobody disputes. Cheap, high signal-to-noise win.
3. **Dimension-first is wrong as a *landing experience*, regardless of what it is as storage.** The Outsider, First Principles Thinker, Contrarian, and Executor (in different ways) all reach this. Vendor engineers arrive knowing their solution name, their BP, or their interface — never their dimension.
4. **`cross-cutting/` is a smell.** The Outsider calls it where architectures die; First Principles calls it an admission the spine is wrong; Executor wants it renamed by enumeration; Expansionist wants it promoted. Nobody defends the current name.
5. **The capability map is a governance artifact, not a filesystem.** First Principles states it explicitly; Outsider, Contrarian, and four of five reviewers endorse the framing. This is the strongest signal in the council.

### Where the council clashes

**The real fight: structural redesign vs. tactical fixes.**

- **First Principles, Outsider, Contrarian (and reviewers 1-5 unanimously)** argue the spine is wrong. The dimension-first tree conflates a governance ontology with storage. Every listed tension — sparse dirs, `foundations/`, `cross-cutting/`, root-file leakage — is a symptom of that conflation. Fix: collapse to `solutions/<name>/` as the single source of truth; capmap, BP, NFR become generated views.
- **Executor** argues the spine is fine, the navigation friction is local, and a structural reorg burns three sprints, breaks external links, and alienates partners who already know where their stuff lives. Ship five fixes Monday; don't relitigate the taxonomy.

Reasonable advisors disagree because they're optimising for different time horizons and risk profiles. Executor is right that *this week* a reorg is reckless. First Principles is right that *next year* the current spine will have grown two more escape hatches and the maintenance cost compounds. Every reviewer named Executor as the biggest blind spot precisely because it refused to engage with the question being asked.

**Secondary clash: how ambitious to get with views.** Expansionist wants a multi-axis catalogue, MCP server, chunked F&T spec — turn the repo into a platform asset. First Principles wants the same architectural shape (one source, many views) but more disciplined scope. Reviewer 5 correctly flags Expansionist for hand-waving migration cost and governance constraints.

### Blind spots the council caught

Peer review surfaced four things no advisor raised:

1. **Ownership and the write path.** Reviewers 1, 2, 4, 5 all flag this. None of the five advisors asked who *writes* into this repo. Structure follows authorship. Without CODEOWNERS, a contribution guide, and a single editor, any structure drifts back to the current state within two releases. **This is the most important missing question.**
2. **Versioning and lifecycle.** Reviewers 2, 3, 4, 5. R3.0 is "partial." R3.1 and R4.0 will add, rename, and deprecate solutions. A structure that churns per release destroys external links regardless of taxonomy.
3. **Governance contractual constraints.** Reviewers 4 and 5. Is the EU programme office contractually requiring capmap-shaped artifacts as deliverables? If yes, "make capmap a generated view" has to produce capmap-shaped output, not just a different storage layout. The Contrarian hinted at this ("are you contractually obliged to mirror?") but didn't push.
4. **Link stability as a hard constraint.** Reviewer 4. The 716kB F&T spec, vendor PRs, external bookmarks all reference current paths. Any reorg has a migration cost denominated in broken links — which Executor over-weights and First Principles under-weights.

### The recommendation

**First Principles is right about the diagnosis. Executor is right about Monday. They are not in conflict, and the council's framing of them as opposed is wrong.**

Adopt this verdict:

1. **Accept First Principles' reframing as the target architecture.** The capability map is a governance ontology. The repo is a documentation catalogue. These are different artefacts with different shapes. The target state is `solutions/<solution-name>/` as the canonical home for every artefact a vendor owns, with capmap/BP/NFR/role as *generated indexes* that link into solutions. This dissolves every listed tension structurally rather than patching them.

2. **Execute Executor's week immediately** as cleanup, not as the answer. Delete duplicate `interoperability/`, fix parent-name duplications, move root files into `foundations/`, add STATUS.md per dimension. These are no-regret moves that improve the repo whether or not the spine is later refactored. Executor's mistake was framing them as a substitute for the structural question; they're a prerequisite.

3. **Before any structural reorg, answer the three blind-spot questions** the reviewers caught:
   - Does the EU programme office contractually require the capmap-shaped tree? If yes, the capmap view must be a real generated artefact, not a wish. If no, the constraint is purely cultural and weaker than assumed.
   - Who owns this repo's structure? Add CODEOWNERS and a contribution guide before adding a single new directory. Structure without ownership reverts.
   - What is the release/versioning model? Tag R3.0 docs before any reorg so external links can pin. A structure that breaks every quarter is worse than any taxonomy debate.

4. **Reject Expansionist's scope** for now. MCP servers and multi-axis knowledge graphs are credible six months after the spine is stable, not before. Reviewer 5's critique is correct.

5. **Reject "dimension-first as the landing experience."** Even keeping the dimension tree as storage, the README must become a flat solution index plus a role-based router ("I'm a vendor / architect / integrator, start here"). This is the Contrarian's and the Outsider's correct point, and it's cheap.

The reason to disagree with the unanimous reviewer chorus that "B wins, D loses" is that the reviewers are scoring an argument, not running a repo. Running a repo means you ship Executor's week while you're answering First Principles' questions. Treating them as either/or is the actual error in the room.

### The one thing to do first

**Write down who owns this repo's structure decision, and whether the EU programme office contractually requires the capmap-shaped tree.**

Not a refactor. Not a rename. A one-page memo, today, that answers: who decides, what is contractually required, and what is merely habit. Every other choice — First Principles' reframe, Executor's fixes, Expansionist's ambitions — is downstream of that answer, and the council unanimously failed to ask it. Until it's answered, any structural change is guessing.

---

*Generated 2026-04-26 13:06 GMT+2 — Council methodology adapted from Andrej Karpathy's LLM Council.*
